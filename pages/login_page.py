import pages.locators.login_locators as loc
from pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, username, password):
        return (
            self._validate_username(username)
            and self._validate_password(password)
            and self.type(loc.USERNAME_INPUT, username)
            and self.type(loc.PASSWORD_INPUT, password)
            and self.click(loc.SUBMIT_BUTTON)
        )

    def _validate_username(self, string):
        return len(string) > 0

    def _validate_password(self, string):
        return len(string) > 0