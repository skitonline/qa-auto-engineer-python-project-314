from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pages.locators.list_structure_locators as list_loc
import pages.locators.tasks_locators as loc
from pages.menu.list_structure_page import ListStructureClass


class TasksPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_tasks()

    def add_task(self, assignee, title, status, content=None, label=None):
        if not self.click(list_loc.CREATE_BUTTON):
            return None

        if not self.fill_fields(assignee, title, status, content, label):
            return None

        if self.wait_url_not_contains('create'):
            result = self.url().rsplit("/", 1)[-1]
        else:
            result = None

        self.open_tasks()
        return result

    def fill_fields(self, assignee, title, status, content, label):
        if (assignee is not None
                and not self._select_option(loc.ASSIGNEE_SELECT, assignee)):
            return False
        if title is not None and not self.type(loc.TITLE_INPUT, title):
            return False
        if content is not None and not self.type(loc.CONTENT_INPUT, content):
            return False
        if (status is not None
                and not self._select_option(loc.STATUS_SELECT, status)):
            return False
        if (label is not None
            and not self._select_option(loc.LABEL_SELECT, label)):
            return False
        if not self.click(list_loc.SAVE_BUTTON):
            return False
        return True

    def _select_option(self, locator, option):
        if not self.click(locator):
            return False

        option_locator = (By.XPATH,
            f'//li[@role="option"][normalize-space(.) = "{option}"]')
        option_el = self.wait_for_element(option_locator)
        if not option_el:
            return False
        self.driver.execute_script("arguments[0].click();", option_el)

        self._close_dropdown()
        return True

    def _close_dropdown(self):
        try:
            backdrops = self.driver.find_elements(*loc.BACKDROP)
            if backdrops:
                self.driver.execute_script("arguments[0].click();", backdrops[0])
        except Exception:
            pass

    def get_all_tasks(self):
        columns = self.wait_for_elements(loc.COLUMN)
        if not columns:
            return {}

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
        cards = self.wait_for_elements(loc.CARD)
        for card in cards:
            if card.get_attribute("data-rfd-draggable-id") == str(id):
                return card
        return None

    def _open_task(self, id):
        task_id = str(id)
        card = self._find_card_by_id(id)
        if not card:
            return False
        locator = (By.CSS_SELECTOR, f'a[href="#/tasks/{task_id}"]')
        return self.click(locator)

    def get_task_info(self, id):
        if not self._open_task(id):
            return None

        return {
            'assignee': self.get_text(loc.ASSIGNEE_SELECT),
            'title': self.get_value(loc.TITLE_INPUT),
            'content': self.get_text(loc.CONTENT_INPUT),
            'status': self.get_text(loc.STATUS_SELECT),
            'label': self.get_text(loc.LABEL_SELECT),
        }

    def edit_task(self, id, assignee=None, title=None,
        status=None, content=None, label=None):
        if not self._open_task(id):
            return None

        if not self._wait_for_record():
            return None

        if not self.fill_fields(assignee, title, status, content, label):
            return None

        self.open_tasks()
        self.wait.until(
            lambda d: '/tasks/' not in d.current_url or d.current_url.endswith('/tasks')
        )
        self.wait_for_elements(loc.COLUMN)
        return True

    def delete_task(self, id):
        if not self._open_task(id):
            return False

        if not self._wait_for_record():
            return False

        if not self.click(list_loc.DELETE_BUTTON):
            return False

        self.wait.until(
            lambda d: self.get_task_by_id(id) is None
        )
        return True

    def filter_by_status(self, status):
        return self._apply_filter(loc.STATUS_SELECT, status)

    def filter_by_assignee(self, assignee):
        return self._apply_filter(loc.ASSIGNEE_SELECT, assignee)

    def filter_by_label(self, label):
        return self._apply_filter(loc.LABEL_SELECT, label)

    def _apply_filter(self, locator, value):
        if not self.click(locator):
            return False
        option_locator = (By.XPATH,
            f'//li[@role="option"][normalize-space(.) = "{value}"]')
        option_el = self.wait_for_element(option_locator)
        if not option_el:
            return False
        self.driver.execute_script("arguments[0].click();", option_el)
        self._close_dropdown()
        self.wait.until(EC.url_contains("filter="))
        self.wait_for_elements(loc.CARD)
        return True

    def get_cards_in_column(self, column_name):
        columns = self.wait_for_elements(loc.COLUMN)

        for column in columns:
            header = column.find_element(*loc.COLUMN_HEADER)
            if column_name in header.text:
                cards = column.find_elements(*loc.CARD)
                return [
                    card.find_element(*loc.CARD_TITLE).text
                    for card in cards
                ]
        return []

    def move_card(self, id, target_column):
        return self.edit_task(id, status=target_column)

    def _wait_for_record(self):
        self.wait.until(self._record_is_loaded)
        return True

    def _record_is_loaded(self, driver):
        return self.get_value(loc.TITLE_INPUT) != ""

    def _find_card_by_id(self, id):
        for _ in range(3):
            cards = self.wait_for_elements(loc.CARD)
            for card in cards:
                try:
                    if card.get_attribute("data-rfd-draggable-id") == str(id):
                        return card
                except Exception:
                    continue
        return None
