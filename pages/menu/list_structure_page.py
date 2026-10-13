from selenium.webdriver.support import expected_conditions as EC

import pages.locators.list_structure_locators as loc
from pages.interface_page import InterfacePage


class ListStructureClass(InterfacePage):
    def _add_element(self, fields):
        if (
            self.click(loc.CREATE_BUTTON)
            and self._fill_data(fields)
        ):
            print('help')
            # возвращаем id из url
            return self.url().rsplit("/", 1)[-1]
        return None

    def _fill_data(self, fields):
        return self._enter_fields(fields) and self.click(loc.SAVE_BUTTON)

    def _create_insert_data(self, locators, values):
        return zip(locators, values)

    def _enter_fields(self, fields):
        return all(self.type(locator, value) for locator, value in fields)
    
    def _get_all_rows(self, fields):
        try:
            rows = self.wait.until(EC.presence_of_all_elements_located(
                loc.ROWS
            ))
        except Exception:
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
        _, id, *fields_row = row.find_elements(*loc.COLUMN)
        data["id"] = id.text
        for i in range(len(fields)):
            field = fields[i]
            data[field] = fields_row[i].text
        return data

    def open_element_by_id(self, id):
        row = self._get_row_by_id(id)
        if row:
            row.click()
            return True
        return None

    def _delete_row(self, id):
        row = self._get_row_by_id(id)

        if not row:
            return False

        checkbox, *_ = row.find_elements(*loc.COLUMN)

        self._select_checkbox(checkbox)
        return self.click(loc.DELETE_BUTTON)

    def delete_some_rows(self, *ids):
        for id in ids:
            if not self._delete_row(id):
                return False
        return True

    def _select_checkbox(self, checkbox):
        if not checkbox.is_selected():
            checkbox.click()

    def delete_all(self):
        el = self.wait.until(EC.presence_of_element_located(loc.SELECT_ALL))
        self.driver.execute_script("arguments[0].click();", el)
        self.click(loc.DELETE_BUTTON)