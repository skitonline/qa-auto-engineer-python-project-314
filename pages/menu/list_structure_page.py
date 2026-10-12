from selenium.webdriver.support import expected_conditions as EC

import pages.locators.list_structure_locators as loc
from pages.interface_page import InterfacePage


class ListStructureClass(InterfacePage):
    def _add_element(self, fields):
        if (
            self.click(loc.CREATE_BUTTON)
            and self._input_fields(fields)
            and self.click(loc.SAVE_BUTTON)
        ):
            # возвращаем id из url
            return self.url().rsplit("/", 1)[-1]
        return None

    def _input_fields(self, fields):
        return all(self.type(locator, value) for locator, value in fields)
    
    def _get_all_rows(self, fields):
        rows = self.wait.until(EC.presence_of_all_elements_located(
            loc.ROWS
        ))

        result = {}
        for row in rows:
            _, id, *row_fields = row.find_elements(*loc.COLUMN)

            row_data = {}
            id = id.text
            for i in range(len(fields)):
                field = fields[i]
                row_data[field] = row_fields[i].text
            result[id] = row_data

        return result

    def _get_row_by_id(self, id):
        rows = self.wait.until(EC.presence_of_all_elements_located(
            loc.ROWS
        ))

        for row in rows:
            try:
                id_cell = row.find_element(*loc.ID_COLUMN)
                cell_text = id_cell.text
                if cell_text == id:
                    return row
            except Exception:
                continue

        return None

    def _get_element_by_id(self, id, fields):
        row = self._get_row_by_id(id)
        if not row:
            return None
        
        data = {}
        _, _, *fields_row = row.find_elements(*loc.COLUMN)
        for i in range(len(fields)):
            field = fields[i]
            data[field] = fields_row[i].text
        return data

    def open_element_by_id(self, id):
        row = self._get_row_by_id(id)
        if row:
            row.click()
        return None