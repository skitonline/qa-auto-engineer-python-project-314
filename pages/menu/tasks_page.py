from pages.interface_page import InterfacePage


class TasksPage(InterfacePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_tasks()