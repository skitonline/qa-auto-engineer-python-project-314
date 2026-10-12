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
            and self._add_element(fields)
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

    def edit_user(self, id, email=None, first_name=None, last_name=None):
        user = self._get_row_by_id(id)
        if not user:
            return False

        email = email or user['email']
        first_name = first_name or user['first_name']
        last_name = last_name or user['last_name']

        if not self._validate(email, first_name, last_name):
            return False

        return self.edit_row(
            {
                self.EMAIL: email,
                self.FIRST_NAME: first_name,
                self.LAST_NAME: last_name
            }
        )