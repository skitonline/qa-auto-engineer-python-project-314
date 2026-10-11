from pages.menu.list_structure_page import ListStructureClass


class LabelsPage(ListStructureClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_labels()