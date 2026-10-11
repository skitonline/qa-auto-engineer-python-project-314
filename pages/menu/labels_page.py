import pages.locators.labels_locators as loc
from pages.menu.list_structure_page import ListStructureClass


class LabelsPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_labels()

    def add_label(self, name):
        fields = [(loc.NAME_INPUT, name)]

        return (
            self._validate_name(name)
            and self.add_element(fields)
        )

    def _validate_name(self, name):
        return len(name) > 0