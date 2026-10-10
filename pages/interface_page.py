import pages.locators.interface_locators as loc
from pages.base_page import BasePage


class InterfacePage(BasePage):
    def logout(self):
        return self.click(loc.PROFILE_ICON) and self.click(loc.LOGOUT_BUTTON)

    def open_dashboard(self):
        self.click(loc.DASHBOARD_LINK)

    def open_users(self):
        self.click(loc.USERS_LINK)

    def open_tasks(self):
        self.click(loc.TASKS_LINK)

    def open_labels(self):
        self.click(loc.LABELS_LINK)

    def open_statuses(self):
        self.click(loc.STATUSES_LINK)

