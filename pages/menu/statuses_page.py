import pages.locators.statuses_locators as loc
from pages.menu.list_structure_page import ListStructureClass


class StatusesPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_statuses()

    def add_status(self, name, slug):
        data = self._create_insert_data(
            loc.LOCATORS,
            [name, slug]
        )

        result = self._add_element(data)

        self.open_statuses()
        return result

    def get_all_statuses(self):
        return self._get_all_rows(loc.FIELDS)

    def get_status_by_id(self, id):
        return self._get_element_by_id(id, loc.FIELDS)

    def edit_status(self, id, name=None, slug=None):
        status = self.open_element_by_id(id)
        if not status:
            return None

        self.wait_for_element(loc.NAME_INPUT)
        if name is None:
            name = self.get_value(loc.NAME_INPUT)
        if slug is None:
            slug = self.get_value(loc.SLUG_INPUT)

        data = self._create_insert_data(
                    loc.LOCATORS,
                    [name, slug]
        )
        return self._fill_data(data)
