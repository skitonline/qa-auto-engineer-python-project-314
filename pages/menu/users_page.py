import re

import pages.locators.list_structure_locators as list_loc
import pages.locators.users_locators as users_loc
from pages.menu.list_structure_page import ListStructureClass


class UsersPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_users()

    def add_user(self, email, first_name, last_name):
        return (
            self._validate_fields(email, first_name, last_name)
            and self.click(list_loc.CREATE_BUTTON)
            and self.type(users_loc.EMAIL_INPUT, email)
            and self.type(users_loc.FIRST_NAME_INPUT, first_name)
            and self.type(users_loc.LAST_NAME_INPUT, last_name)
            and self.click(list_loc.SAVE_BUTTON)
        )

    def _validate_fields(self, email, first_name, last_name):
        return (
            self._validate_email(email)
            and self._validate_first_name(first_name)
            and self._validate_last_name(last_name)
        )

    def _validate_fields(self, email, first_name, last_name):
        return (
            self._validate_email(email)
            and self._validate_first_name(first_name)
            and self._validate_last_name(last_name)
        )

    def _validate_email(self, email):
        return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

    def _validate_first_name(self, first_name):
        return len(first_name) > 0

    def _validate_last_name(self, last_name):
        return len(last_name) > 0