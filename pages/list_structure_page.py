from pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
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

    def get_all_rows(self, columns):
        result = []

        while True:
            rows = self.driver.find_elements(*self.ROW)

            for row in rows:
                cells = row.find_elements(*self.CELL_IN_ROW)
                checkbox_cell, id_cell, *fields_cells = cells

                checkbox_input = checkbox_cell.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
                is_checked = self.driver.execute_script("return arguments[0].checked;", checkbox_input)
                id = id_cell.text

                row = {}
                row[id] = {'checkbox' : is_checked}
                for i in range(len(columns)):
                    row[id][columns[i]] = fields_cells[i].text

                result.append(row)

            if not self.click(self.NEXT_ICON):
                break

            # Даём браузеру время начать рендер (это спасает от Stale внутри ожидания)
            time.sleep(0.5)
        #print(result)
        return result


    def edit_row(self, data):
        pass
