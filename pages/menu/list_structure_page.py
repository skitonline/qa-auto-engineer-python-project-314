from selenium.webdriver.support import expected_conditions as EC

import pages.locators.list_structure_locators as loc
from pages.interface_page import InterfacePage


class ListStructureClass(InterfacePage):
    def add_element(self, fields):
        if (
            self.click(loc.CREATE_BUTTON)
            and self._input_fields(fields)
            and self.click(loc.SAVE_BUTTON)
        ):
            # возвращаем id из url
            return self.url().rsplit("/", 1)[-1]
        else:
            return None

    def _input_fields(self, fields):
        return all(self.type(locator, value) for locator, value in fields)
    
    def _get_all_rows(self, fields):
        # Ждём, пока таблица появится и в ней будут строки
        tbody = self.wait.until(EC.presence_of_element_located(loc.TABLE))
        rows = tbody.find_elements(*loc.ROWS)

        result = {}
        for row in rows:
            # Находим ячейки в строке
            cells = row.find_elements(*loc.CELLS)

            # В ячейках есть span с текстом — берём innerText через text
            def get_text(cell_index):
                try:
                    span = cells[cell_index].find_element(*loc.SPAN)
                    return span.text or ''
                except Exception:
                    return ''

            row_data = {}
            for i in range(len(fields)):
                field = fields[i]
                row_data[field] = get_text(i + 1)
            id = get_text(0)
            result[id] = row_data

        return result



