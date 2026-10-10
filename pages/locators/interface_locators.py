from selenium.webdriver.common.by import By

PROFILE_ICON = (By.CSS_SELECTOR, 'button[aria-label="Profile"]')
LOGOUT_BUTTON = (By.CLASS_NAME, "logout")

DASHBOARD_LINK = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/"]')
USERS_LINK = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/users"]')
TASKS_LINK = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/tasks"]')
LABELS_LINK = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/labels"]')
STATUSES_LINK = (By.CSS_SELECTOR, 'a[role="menuitem"][href="#/task_statuses"]')