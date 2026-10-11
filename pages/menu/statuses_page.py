import pages.locators.statuses_locators as loc
from pages.menu.list_structure_page import ListStructureClass


class StatusesPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_statuses()

    def add_status(self, name, slug):
        fields = [
            (loc.NAME_INPUT, name), 
            (loc.SLUG_INPUT, slug)
        ]

        result = (
            self._validate_name(name)
            and self._validate_slug(slug)
            and self.add_element(fields)
        )

        self.open_statuses()
        return result

    def _validate_name(self, name):
        return len(name) > 0

    def _validate_slug(self, slug):
        return len(slug) > 0

    def get_all_statuses(self):
        return self._get_all_rows(loc.FIELDS)

    def get_status_by_id(self, id):
        statuses = self.get_all_statuses()
        return statuses.get(id)