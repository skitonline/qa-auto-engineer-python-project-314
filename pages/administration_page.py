from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdministrationPage(BasePage):
    PROFILE = (By.CSS_SELECTOR, 'button[aria-label="Profile"]')
    LOGOUT_TEXT = (By.XPATH, '//span[normalize-space()="Logout"]')

    DASHBOARD = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/"]')
    USERS = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/users"]')
    TASKS = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/tasks"]')
    LABELS = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/labels"]')
    TASK_STATUSES = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/task_statuses"]')

    def logout(self):
        self.click(self.PROFILE)
        
        logout_span = self.wait.until(EC.presence_of_element_located(self.LOGOUT_TEXT))
        self.wait.until(lambda d: logout_span.size['height'] > 0)
        parent_li = logout_span.find_element(By.XPATH, './ancestor::li[1]')
        self.click(parent_li)


    def open_dashboard(self):
        self.click(self.DASHBOARD)


    def open_users(self):
        self.click(self.USERS)


    def open_tasks(self):
        self.click(self.TASKS)


    def open_labels(self):
        self.click(self.LABELS)


    def open_task_statuses(self):
        self.click(self.TASK_STATUSES)

