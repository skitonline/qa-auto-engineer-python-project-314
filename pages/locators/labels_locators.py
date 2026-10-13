from selenium.webdriver.common.by import By

NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
LOCATORS = (NAME_INPUT, )

FIELDS = ('name', 'created_at')