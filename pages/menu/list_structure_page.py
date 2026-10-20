from selenium.webdriver.support import expected_conditions as EC

import pages.locators.list_structure_locators as loc
from pages.interface_page import InterfacePage


class ListStructureClass(InterfacePage):
    def _add_element(self, fields):
        if not self.click(loc.CREATE_BUTTON):
            return None
        if not self._fill_data(fields):
            return None

        if self.wait_url_not_contains('create'):
            return self.url().rsplit("/", 1)[-1]
        return None

    def _fill_data(self, fields):
        return self._enter_fields(fields) and self.click(loc.SAVE_BUTTON)

    def _create_insert_data(self, locators, values):
        return zip(locators, values)

    def _enter_fields(self, fields):
        return all(self.type(locator, value) for locator, value in fields)

    def _get_all_rows(self, fields):
        rows = self.wait_for_elements(loc.ROWS)
        if not rows:
            return None

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
        rows = self.wait_for_elements(loc.ROWS)
        if not rows:
            return None

        for row in rows:
            id_cell = row.find_element(*loc.ID_COLUMN)
            cell_text = id_cell.text
            if cell_text == id:
                return row

        return None

    def _get_element_by_id(self, id, fields):
        row = self._get_row_by_id(id)
        if not row:
            return None

        data = {}
        _, id_el, *fields_row = row.find_elements(*loc.COLUMN)
        data["id"] = id_el.text
        for i in range(len(fields)):
            field = fields[i]
            data[field] = fields_row[i].text
        return data

    def open_element_by_id(self, id):
        row = self._get_row_by_id(id)
        if row:
            row.click()
            return row
        return None

    def delete_some_rows(self, *ids):
        rows = self.wait_for_elements(loc.ROWS)
        before_delete = len(rows)
        ids_str = {str(i) for i in ids}

        for row in rows:
            row_id = row.find_element(*loc.ID_COLUMN).text
            if row_id in ids_str:
                checkbox = row.find_element(*loc.CHECKBOX)
                self._select_checkbox(checkbox)

        self.click(loc.DELETE_BUTTON)
        after_delete = len(self.wait_for_elements(loc.ROWS))
        return before_delete - after_delete == len(ids)

    def _select_checkbox(self, checkbox):
        if not checkbox.is_selected():
            checkbox.click()

    def delete_all(self):
        el = self.wait.until(EC.presence_of_element_located(loc.SELECT_ALL))
        el.click()
        self.click(loc.DELETE_BUTTON)
        self.wait.until(self._is_table_empty)

    @staticmethod
    def _is_table_empty(driver):
        rows = driver.find_elements(*loc.ROWS)
        return len(rows) == 0
