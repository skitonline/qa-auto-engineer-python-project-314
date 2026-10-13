from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="firstName"]')
LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="lastName"]')
LOCATORS = (EMAIL_INPUT, FIRST_NAME_INPUT, LAST_NAME_INPUT)

FIELDS = ('email', 'first_name', 'last_name', 'created_at')
