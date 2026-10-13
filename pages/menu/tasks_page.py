from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pages.locators.list_structure_locators as list_loc
import pages.locators.tasks_locators as loc
from pages.menu.list_structure_page import ListStructureClass


class TasksPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_tasks()

    def add_task(self, title, status, assignee, label=None, content=None):
        """Создаёт задачу и возвращает её id (или None при ошибке)."""
        if not (
            self._validate_title(title)
            and self._validate_status(status)
            and self._validate_assignee(assignee)
        ):
            return None

        if not self.click(list_loc.CREATE_BUTTON):
            return None

        if not self.type(loc.TITLE_INPUT, title):
            return None

        if not self._select_option(loc.STATUS_INPUT, status):
            return None

        if not self._select_option(loc.ASSIGNEE_INPUT, assignee):
            return None

        if label and not self._select_option(loc.LABEL_INPUT, label):
            return None

        if content and not self.type(loc.CONTENT_INPUT, content):
            return None

        self._close_dropdown()

        # запоминаем адрес страницы создания до нажатия Save
        current_url = self.url()
        if not self.click(list_loc.SAVE_BUTTON):
            return None

        # после сохранения приложение переходит на страницу новой задачи,
        # из адреса этой страницы берём её id
        try:
            self.wait.until(EC.url_changes(current_url))
            task_id = self.url().rsplit("/", 1)[-1]
        except Exception:
            return None

        self.open_tasks()
        return task_id

    def _validate_title(self, title):
        return len(title) > 0

    def _validate_status(self, status):
        return len(status) > 0

    def _validate_assignee(self, assignee):
        return len(assignee) > 0

    def _select_option(self, input_locator, option_text):
        """Открывает выпадающий список и выбирает в нём пункт по тексту."""
        try:
            # ждём, пока закроется предыдущий список — иначе он перекроет новый
            self.wait.until(EC.invisibility_of_element_located(loc.SELECT_LISTBOX))

            native = self.wait.until(
                EC.presence_of_element_located(input_locator)
            )
            # у списка есть скрытый input и видимый элемент (combobox)
            select = native.find_element(By.XPATH, "..").find_element(
                *loc.SELECT_COMBOBOX
            )
            select.click()
            # ждём, пока откроется список
            self.wait.until(EC.presence_of_element_located(loc.SELECT_LISTBOX))
            # ждём нужный пункт и выбираем его; пока список открывается,
            # его пункты могут перекрывать друг друга, поэтому при перехвате
            # клика пробуем ещё раз
            option = (
                By.XPATH,
                f"//li[@role='option'][normalize-space(.)='{option_text}']",
            )
            for _ in range(3):
                try:
                    item = self.wait.until(EC.element_to_be_clickable(option))
                    item.click()
                    break
                except ElementClickInterceptedException:
                    continue
            else:
                return False
        except Exception:
            return False

        # после выбора пункта список одиночного выбора закрывается сам;
        # ждём закрытия, чтобы его пункты не перекрывали следующий список
        try:
            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(loc.SELECT_LISTBOX)
            )
        except Exception:
            pass  # мультиселект (метка) остаётся открытым — закроем позже

        return True

    def get_options(self, input_locator):
        """Открывает список и возвращает тексты его пунктов."""
        # ждём, пока закроется предыдущий список — иначе он перекроет новый
        self.wait.until(EC.invisibility_of_element_located(loc.SELECT_LISTBOX))

        native = self.wait.until(
            EC.presence_of_element_located(input_locator)
        )
        select = native.find_element(By.XPATH, "..").find_element(
            *loc.SELECT_COMBOBOX
        )
        select.click()
        self.wait.until(EC.presence_of_element_located(loc.SELECT_LISTBOX))

        options = []
        for option in self.driver.find_elements(*loc.SELECT_OPTION):
            if option.text.strip():
                options.append(option.text.strip())

        self._close_dropdown()
        return options

    def _close_dropdown(self):
        """Закрывает открытый выпадающий список (нужно после выбора метки)."""
        try:
            self.driver.find_element(*loc.MODAL_BACKDROP).click()
        except Exception:
            pass

    def get_all_tasks(self):
        """Возвращает все задачи с доски."""
        columns = self.wait.until(
            EC.presence_of_all_elements_located(loc.COLUMN)
        )

        result = {}
        for column in columns:
            header = column.find_element(*loc.COLUMN_HEADER)
            status = header.text
            for card in column.find_elements(*loc.CARD):
                content = card.find_elements(*loc.CARD_CONTENT)
                result[card.get_attribute("data-rfd-draggable-id")] = {
                    "title": card.find_element(*loc.CARD_TITLE).text,
                    "status": status,
                    "content": content[0].text if content else "",
                }
        return result

    def get_task_by_id(self, id):
        """Возвращает данные задачи по id (None, если задачи нет на доске)."""
        tasks = self.get_all_tasks()
        if not tasks:
            return None
        return tasks.get(str(id))

    def get_cards_in_column(self, column_name):
        """Возвращает заголовки карточек в колонке с указанным названием."""
        columns = self.wait.until(
            EC.presence_of_all_elements_located(loc.COLUMN)
        )

        for column in columns:
            header = column.find_element(*loc.COLUMN_HEADER)
            if column_name in header.text:
                cards = column.find_elements(*loc.CARD)
                return [
                    card.find_element(*loc.CARD_TITLE).text
                    for card in cards
                ]
        return None

    def edit_task(
        self, id, title=None, status=None, assignee=None, label=None,
        content=None,
    ):
        """Открывает задачу, изменяет переданные поля и сохраняет."""
        if not self._open_task(id):
            return None

        # ждём, пока форма заполнится данными задачи
        if not self._wait_for_record():
            return None

        if title is not None and not self.type(loc.TITLE_INPUT, title):
            return None
        if status is not None and not self._select_option(
            loc.STATUS_INPUT, status
        ):
            return None
        if assignee is not None and not self._select_option(
            loc.ASSIGNEE_INPUT, assignee
        ):
            return None
        if label is not None and not self._select_option(
            loc.LABEL_INPUT, label
        ):
            return None
        if content is not None and not self.type(loc.CONTENT_INPUT, content):
            return None

        self._close_dropdown()

        if not self.click(list_loc.SAVE_BUTTON):
            return False

        # после сохранения приложение возвращается на доску задач
        try:
            self.wait.until(
                EC.presence_of_all_elements_located(loc.COLUMN)
            )
        except Exception:
            return False
        return True

    def delete_task(self, id):
        """Удаляет задачу и возвращается на доску."""
        if not self._open_task(id):
            return False

        # ждём, пока форма заполнится данными задачи
        if not self._wait_for_record():
            return False

        if not self.click(list_loc.DELETE_BUTTON):
            return False

        # после удаления приложение возвращается на доску задач
        try:
            self.wait.until(
                EC.presence_of_all_elements_located(loc.COLUMN)
            )
        except Exception:
            return False
        return True

    def filter_by_status(self, status):
        return self._apply_filter(loc.STATUS_FILTER, status)

    def filter_by_assignee(self, assignee):
        return self._apply_filter(loc.ASSIGNEE_FILTER, assignee)

    def filter_by_label(self, label):
        return self._apply_filter(loc.LABEL_FILTER, label)

    def _apply_filter(self, locator, value):
        # запоминаем, сколько карточек было на доске до фильтрации
        self._cards_before = self._count_cards()

        if not self._select_option(locator, value):
            return False

        # ждём, пока фильтр применится: в адресе появится параметр filter
        try:
            self.wait.until(EC.url_contains("filter="))
            # и пока доска обновится (количество карточек изменится)
            self.wait.until(self._board_has_changed)
        except Exception:
            return False
        return True

    def _board_has_changed(self, driver):
        """True, когда количество карточек на доске изменилось."""
        return self._count_cards() != self._cards_before

    def _count_cards(self):
        return len(self.driver.find_elements(*loc.CARD))

    def move_card(self, title, target_column):
        """Переносит карточку в другую колонку (сменой статуса в форме)."""
        card = self._find_card_by_title(title)
        if not card:
            return False
        task_id = card.get_attribute("data-rfd-draggable-id")
        return self.edit_task(task_id, status=target_column)

    def _open_task(self, id):
        """Открывает задачу на редактирование через кнопку Edit на карточке."""
        self.open_tasks()
        card = self._find_card_by_id(id)
        if not card:
            return False
        card.find_element(*loc.CARD_EDIT_BUTTON).click()
        return True

    def _wait_for_record(self):
        """Ждёт, пока форма заполнится данными открытой задачи."""
        try:
            self.wait.until(self._record_is_loaded)
            return True
        except Exception:
            return False

    def _record_is_loaded(self, driver):
        """True, когда в форме появились данные задачи."""
        return self.get_text_from_field(loc.TITLE_INPUT) != ""

    def _find_card_by_title(self, title):
        """Ищет карточку задачи на доске по заголовку."""
        cards = self.wait.until(
            EC.presence_of_all_elements_located(loc.CARD)
        )

        for card in cards:
            if title in card.find_element(*loc.CARD_TITLE).text:
                return card
        return None

    def _find_card_by_id(self, id):
        """Ищет карточку задачи на доске по её id."""
        cards = self.wait.until(
            EC.presence_of_all_elements_located(loc.CARD)
        )

        for card in cards:
            if card.get_attribute("data-rfd-draggable-id") == str(id):
                return card
        return None