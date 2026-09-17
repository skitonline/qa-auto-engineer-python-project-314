from pages.list_structure_page import ListStructureClass
from selenium.webdriver.common.by import By

class LabelsPage(ListStructureClass):
    NAME = (By.CSS_SELECTOR, 'input[name="name"]')

    COLUMNS = ('name', 'created_at')

    def __init__(self, driver):
        super().__init__(driver)
        self.open_labels()

    def add_label(self, name):
        if not self._validate(name):
            return False

        result = self.add_element({self.NAME : name})
        self.open_labels()
        return result

    def _validate(self, name):
        return len(name) > 0

    def get_labels(self):
        return self.get_all_rows(self.COLUMNS)

    def get_label_by_id(self, label_id):
        row = self.get_element_by_id(label_id)
        if row is None:
            return False

        data = {}  
        cells = row.find_elements(*self.CELL_IN_ROW)
        _, _, *fields_cells = cells
        for i in range(len(self.COLUMNS)):
            data[self.COLUMNS[i]] = fields_cells[i].text

        row.click()
        return data

    def edit_label(self, label_id, name=None):
        label = self.get_label_by_id(label_id)
        if label is None:
            return False

        if not self._validate(name):
            return False

        result = self.edit_row({self.NAME : name})

        return result