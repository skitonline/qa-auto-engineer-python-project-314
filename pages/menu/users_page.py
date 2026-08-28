from pages.list_structure_page import ListStructureClass
from selenium.webdriver.common.by import By
import re


class UsersPage(ListStructureClass):
    EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastName"]')

    COLUMNS = ('email', 'first_name', 'last_name', 'created_at')


    def __init__(self, driver):
        super().__init__(driver)
        self.open_users()

    
    def add_user(self, email, first_name, last_name):
        if not (self.validate_email(email) \
                and self.validate_first_name(first_name) \
                and self.validate_last_name(last_name)):
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
    def validate_email(self, email):
        return self.EMAIL_PATTERN.match(email) is not None

    
    def validate_first_name(self, first_name):
        return len(first_name)


    def validate_last_name(self, last_name):
            return len(last_name)


    def get_users(self):
        return self.get_all_rows(self.COLUMNS)
