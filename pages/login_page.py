import pages.locators.login_locators as loc
from pages.base_page import BasePage


class LoginPage(BasePage):
    
    def login(self, username, password):
        return (
            self._validate_fields(username, password)
            and self.type(loc.USERNAME_INPUT, username)
            and self.type(loc.PASSWORD_INPUT, password)
            and self.click(loc.SUBMIT_BUTTON)
        )

    def _validate_fields(self, login, password):
        return self._validate_email(login) and self._validate_password(password)

    def _validate_email(self, string):
        return len(string) > 0

    def _validate_password(self, string):
        return len(string) > 0