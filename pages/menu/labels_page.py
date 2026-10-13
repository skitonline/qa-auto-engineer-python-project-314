import pages.locators.labels_locators as loc
from pages.menu.list_structure_page import ListStructureClass


class LabelsPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_labels()

    def add_label(self, name):
        data = self._create_insert_data(loc.LOCATORS, [name, ])

        result = self._validate_name(name) and self._add_element(data)
        print(result)

        self.open_labels()
        return result

    def _validate_name(self, name):
        return len(name) > 0

    def get_all_labels(self):
        return self._get_all_rows(loc.FIELDS)

    def get_label_by_id(self, id):
        return self._get_element_by_id(id, loc.FIELDS)

    def edit_label(self, id, name=None):
        label = self.open_element_by_id(id)
        if not label:
            return None

        name = name or self.get_text_from_field(loc.NAME_INPUT)

        data = self._create_insert_data(loc.LOCATORS, [name, ])
        return self._validate_name(name) and self._fill_data(data)
