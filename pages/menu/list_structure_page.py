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
        for _ in range(3):
            rows = self.wait_for_elements(loc.ROWS)
            if not rows:
                return None

            for row in rows:
                try:
                    id_cell = row.find_element(*loc.ID_COLUMN)
                    if id_cell.text == id:
                        return row
                except Exception:
                    continue

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
        ids_str = {str(i) for i in ids}

        for row in rows:
            row_id = row.find_element(*loc.ID_COLUMN).text
            if row_id in ids_str:
                checkbox = row.find_element(*loc.CHECKBOX)
                self._select_checkbox(checkbox)

        self.click(loc.DELETE_BUTTON)
        return self._wait_until_rows_absent(ids)

    def _select_checkbox(self, checkbox):
        if not checkbox.is_selected():
            checkbox.click()

    def delete_all(self):
        el = self.wait.until(EC.presence_of_element_located(loc.SELECT_ALL))
        el.click()
        self.click(loc.DELETE_BUTTON)
        return self._wait_until_rows_absent()

    def _wait_until_row_updated(self, id, fields, expected):
        self._wait_undo_window_closed()
        self.open(self._resource_list_url())
        self.wait_for_elements(loc.ROWS)

        def row_is_updated(driver, value=id):
            row = self._find_row(value)
            if row is None:
                return False
            return self._row_has_values(row, fields, expected)

        try:
            self.wait.until(row_is_updated)
            return True
        except Exception:
            return False

    def _wait_until_rows_absent(self, ids=None):
        self._wait_undo_window_closed()
        self.open(self._resource_list_url())
        self.wait_for_elements(loc.ROWS)
        ids_set = None if ids is None else {str(i) for i in ids}

        def rows_are_absent(driver, value=ids_set):
            return self._all_rows_absent(value)

        try:
            self.wait.until(rows_are_absent)
            return True
        except Exception:
            return False

    def _find_row(self, id):
        rows = self.driver.find_elements(*loc.ROWS)
        for row in rows:
            try:
                id_cell = row.find_element(*loc.ID_COLUMN)
                if id_cell.text == str(id):
                    return row
            except Exception:
                continue
        return None

    def _row_has_values(self, row, fields, expected):
        cells = row.find_elements(*loc.COLUMN)
        if len(cells) < len(fields) + 2:
            return False
        row_fields = cells[2:]
        for i, field in enumerate(fields):
            if field in expected and row_fields[i].text != expected[field]:
                return False
        return True

    def _all_rows_absent(self, ids_set):
        rows = self.driver.find_elements(*loc.ROWS)
        if ids_set is None:
            return len(rows) == 0
        found = set()
        for row in rows:
            try:
                found.add(row.find_element(*loc.ID_COLUMN).text)
            except Exception:
                continue
        return not (ids_set & found)
