import pages.locators.users_locators as locs
from pages.menu.list_structure_page import ListStructureClass


class UsersPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_users()

    def add_user(self, email, first_name, last_name):
        data = self._create_insert_data(
            locs.LOCATORS,
            [email, first_name, last_name]
        )

        result = self._add_element(data)

        self.open_users()
        return result

    def get_all_users(self):
        return self._get_all_rows(locs.FIELDS)

    def get_user_by_id(self, id):
        return self._get_element_by_id(id, locs.FIELDS)

    def edit_user(self, id, email=None, first_name=None, last_name=None):
        user = self.open_element_by_id(id)
        if not user:
            return None

        self.wait_for_element(locs.EMAIL_INPUT)
        if email is None:
            email = self.get_value(locs.EMAIL_INPUT)
        if first_name is None:
            first_name = self.get_value(locs.FIRST_NAME_INPUT)
        if last_name is None:
            last_name = self.get_value(locs.LAST_NAME_INPUT)

        data = self._create_insert_data(
                    locs.LOCATORS,
                    [email, first_name, last_name]
        )
        result = self._fill_data(data)
        if not result:
            return result

        self.open_users()
        if not self._wait_until_row_updated(
                id, locs.FIELDS,
                {'email': email, 'first_name': first_name,
                 'last_name': last_name}):
            return False
        return result
