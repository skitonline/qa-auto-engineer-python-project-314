import re

import pages.locators.users_locators as loc
from pages.menu.list_structure_page import ListStructureClass


class UsersPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_users()

    def add_user(self, email, first_name, last_name):
        fields = [
            (loc.EMAIL_INPUT, email), 
            (loc.FIRST_NAME_INPUT, first_name), 
            (loc.LAST_NAME_INPUT, last_name)
        ]

        result = (
            self._validate_email(email)
            and self._validate_first_name(first_name)
            and self._validate_last_name(last_name)
            and self.add_element(fields)
        )

        self.open_users()
        return result

    def _validate_email(self, email):
        return re.match(r'^[^@]+@[^@]+\.[^@]+$', email) is not None

    def _validate_first_name(self, first_name):
        return len(first_name) > 0

    def _validate_last_name(self, last_name):
        return len(last_name) > 0

    def get_all_users(self):
        return self._get_all_rows(loc.FIELDS)

    def get_user_by_id(self, id):
        return self._get_element_by_id(id, loc.FIELDS)