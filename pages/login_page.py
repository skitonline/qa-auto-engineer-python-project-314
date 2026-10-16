import pages.locators.login_locators as loc
from pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, username, password):
        if not (self.wait_for_element(loc.USERNAME_INPUT)
                and self.type(loc.USERNAME_INPUT, username)
                and self.type(loc.PASSWORD_INPUT, password)
                and self.click(loc.SUBMIT_BUTTON)):
            return False

        return self.wait_url_not_contains("login")
