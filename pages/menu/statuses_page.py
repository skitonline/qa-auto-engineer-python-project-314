from pages.list_structure_page import ListStructureClass
from selenium.webdriver.common.by import By

class StatusesPage(ListStructureClass):
    NAME = (By.CSS_SELECTOR, 'input[name="name"]')
    SLUG = (By.CSS_SELECTOR, 'input[name="slug"]')

    COLUMNS = ('name', 'slug', 'created_at')


    def __init__(self, driver):
        super().__init__(driver)
        self.open_statuses()

    
    def add_status(self, name, slug):
        if not self._validate(name, slug):
            return False

        result = self.add_element(
            {
                self.NAME : name,
                self.SLUG : slug
            }
        )
        self.open_statuses()
        return result

    
    def _validate(self, name, slug):
        return self._validate_name(name) and self._validate_slug(slug)

    def _validate_name(self, name):
        return len(name) > 0

    def _validate_slug(self, slug):
        return len(slug) > 0


    def get_statuses(self):
        return self.get_all_rows(self.COLUMNS)

    def get_status_by_id(self, status_id):
        row = self.get_element_by_id(status_id)
        if row is None:
            return False

        data = {}
        cells = row.find_elements(*self.CELL_IN_ROW)
        _, _, *fields_cells = cells
        for i in range(len(self.COLUMNS)):
            data[self.COLUMNS[i]] = fields_cells[i].text

        row.click()
        return data

    def edit_status(self, status_id, name=None, slug=None):
        status = self.get_status_by_id(status_id)
        if status is None:
            return False

        if not self._validate(name, slug):
            return False

        result = self.edit_row(
            {
                self.NAME : name,
                self.SLUG : slug
            }
        )

        return result