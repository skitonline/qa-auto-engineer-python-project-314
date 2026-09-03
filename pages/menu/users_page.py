from pages.list_structure_page import ListStructureClass
from selenium.webdriver.common.by import By
import re


class UsersPage(ListStructureClass):
    EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastName"]')

    EMAIL_EDIT_FORM = (By.NAME, "email")
    FIRST_NAME_EDIT_FORM = (By.NAME, "firstName")
    LAST_NAME_EDIT_FORM = (By.NAME, "lastName")

    COLUMNS = ('email', 'first_name', 'last_name', 'created_at')


    def __init__(self, driver):
        super().__init__(driver)
        self.open_users()

    
    def add_user(self, email, first_name, last_name):
        if not self._validate(email, first_name, last_name):
            return False

        result = self.add_element(
            {
                self.EMAIL : email,
                self.FIRST_NAME : first_name,
                self.LAST_NAME : last_name
            }
        )
        self.open_users()
        return result


    EMAIL_PATTERN = re.compile(r'^\S+@\S+\.\S+$')
    def _validate(self, email, first_name, last_name):
        return (self._validate_email(email) \
                and self._validate_first_name(first_name) \
                and self._validate_last_name(last_name))
    
    
    def _validate_email(self, email):
        return self.EMAIL_PATTERN.match(email) is not None

    
    def _validate_first_name(self, first_name):
        return len(first_name)


    def _validate_last_name(self, last_name):
            return len(last_name)


    def get_users(self):
        return self.get_all_rows(self.COLUMNS)


    def get_user_by_id(self, user_id, go_into_row=False):
        row = self.get_element_by_id(user_id, self.COLUMNS)
        if row is None:
            return False

        data = {}
        cells = row.find_elements(*self.CELL_IN_ROW)
        _, _, *fields_cells = cells
        for i in range(len(self.COLUMNS)):
            data[self.COLUMNS[i]] = fields_cells[i].text

        if go_into_row:
            row.click()

        return data


    def edit_user(self, user_id, email=None, first_name=None, last_name=None):
        user = self.get_user_by_id(user_id)
        if user is None:
            return False

        email = email or user['email']
        first_name = first_name or user['first_name']
        last_name = last_name or user['last_name']

        if not self._validate(email, first_name, last_name):
            return False

        result = self.edit_row(
            {
                self.EMAIL_EDIT_FORM : email,
                self.FIRST_NAME_EDIT_FORM : first_name,
                self.LAST_NAME_EDIT_FORM : last_name
            }
        )
        
        return result