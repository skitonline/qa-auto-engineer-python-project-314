from pages.administration_page import AdministrationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class UsersPage(AdministrationPage):
    CREATE = (By.CSS_SELECTOR, 'a[aria-label="Create"]')

    EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastName"]')

    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Save"]')
    CREATE_DONE = (By.XPATH, '//div[normalize-space()="Element created"]')

    def add_user(self, email, first_name, last_name):
        self.click(self.CREATE)

        self.type(self.EMAIL, email)
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)

        self.click(self.SAVE_BUTTON)
        try:
            self.driver.find_element(*self.CREATE_DONE)
            return True
        except NoSuchElementException:
            return False