import pages.locators.list_structure_locators as loc
from pages.interface_page import InterfacePage


class ListStructureClass(InterfacePage):
    def add_element(self, fields):
        return (
            self.click(loc.CREATE_BUTTON)
            and self._input_fields(fields)
            and self.click(loc.SAVE_BUTTON)
        )

    def _input_fields(self, fields):
        return all(self.type(locator, value) for locator, value in fields)


