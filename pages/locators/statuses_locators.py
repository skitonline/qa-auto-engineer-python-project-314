from selenium.webdriver.common.by import By

NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
SLUG_INPUT = (By.CSS_SELECTOR, 'input[name="slug"]')
LOCATORS = (NAME_INPUT, SLUG_INPUT)

FIELDS = ('name', 'slug', 'created_at')