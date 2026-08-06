from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[autocomplete="username"]')
    PASSWORD = (By.CSS_SELECTOR, '[autocomplete="current-password"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    WELCOME = (By.ID, 'react-admin-title')
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, 'div.RaNotification-error')


    def wait_for_notification_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.ERROR_NOTIFICATION))


    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.wait_for_notification_to_disappear()
        self.click(self.SUBMIT)