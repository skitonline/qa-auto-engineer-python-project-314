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

        return (
            self._validate_name(name)
            and self._validate_slug(slug)
            and self.add_element(fields)
        )

    def _validate_name(self, name):
        return len(name) > 0

    def _validate_slug(self, slug):
        return len(slug) > 0