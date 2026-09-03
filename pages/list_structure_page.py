from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ListStructureClass(MainPage):
    CREATE_BTN = (By.CSS_SELECTOR, 'a[aria-label="Create"]')
    SAVE_BTN = (By.CSS_SELECTOR, '[aria-label="Save"]')
    CREATE_DONE = (By.XPATH, '//div[normalize-space()="Element created"]')

    COUNT_COUNTAINS = (By.CSS_SELECTOR, 'p.MuiTablePagination-displayedRows')

    DELETE_BTN = (By.CSS_SELECTOR, '[aria-label="Delete"]')
    SELECT_ALL = (By.CSS_SELECTOR, '[aria-label="Select all"]')

    def add_element(self, dict_values):
        self.click(self.CREATE_BTN)

        for locator, value in dict_values.items():
            self.type(locator, value)

        self.click(self.SAVE_BTN)

        return self.is_displayed(self.CREATE_DONE)


    def how_many_elements_countains(self):
        #строка вида '1-8 of 8'
        count = self.text_of(self.COUNT_COUNTAINS)
        return int(count.split("of")[1])


    ROW = (By.CSS_SELECTOR, "tbody tr")
    CELL_IN_ROW = (By.TAG_NAME, "td")
    NEXT_ICON = (By.CSS_SELECTOR, 'button[aria-label="Go to next page"]')

    def _go_to_next_page(self):
        buttons = self.driver.find_elements(*self.NEXT_ICON)
        if not buttons:
            return False

        btn = buttons[0]
        if not btn.is_displayed() or not btn.is_enabled():
            return False
        if btn.get_attribute("aria-disabled") == "true":
            return False

        rows = self.driver.find_elements(*self.ROW)
        first = rows[0] if rows else None
        btn.click()
        if first is not None:
            self.wait.until(EC.staleness_of(first))
        return True

    def get_all_rows(self, columns):
        result = {}

        while True:
            page_rows = self.driver.execute_script(
                """
                return Array.from(document.querySelectorAll('tbody tr')).map(row => {
                    const cells = Array.from(row.querySelectorAll('td'));
                    const checkbox = cells[0]
                        && cells[0].querySelector('input[type="checkbox"]');
                    return {
                        id: cells[1] ? cells[1].innerText.trim() : '',
                        checkbox: !!(checkbox && checkbox.checked),
                        fields: cells.slice(2).map(c => c.innerText.trim())
                    };
                });
                """
            )

            for row in page_rows:
                item = {"checkbox": row["checkbox"]}
                for i, col in enumerate(columns):
                    item[col] = row["fields"][i] if i < len(row["fields"]) else ""
                result[row["id"]] = item

            if not self._go_to_next_page():
                break

        return result


    def get_element_by_id(self, id_row):
        id_row = str(id_row)

        while True:
            rows = self.driver.find_elements(*self.ROW)
            for row in rows:
                cells = row.find_elements(*self.CELL_IN_ROW)
                id = cells[1].text
                if id == id_row:
                    return row
            if not self._go_to_next_page():
                break
        return None

    def edit_row(self, new_row_data):
        for locator, value in new_row_data.items():
            self.fill_field(locator, value)
        return self.click(self.SAVE_BTN)


    def delete_row(self, row_id):
        row = self.get_element_by_id(row_id)
        checkbox_cell = row.find_elements(*self.CELL_IN_ROW)[0]
        checkbox = checkbox_cell.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        is_checked = self.driver.execute_script("return arguments[0].checked;", checkbox)
        if not is_checked:
            checkbox.click()
            self.click(self.DELETE_BTN)
            return True
        return False 
