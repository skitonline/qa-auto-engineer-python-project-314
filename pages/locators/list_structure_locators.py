from selenium.webdriver.common.by import By

CREATE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="Create"]')
SAVE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Save"]')
DELETE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Delete"]')
SELECT_ALL = (By.CSS_SELECTOR, '[aria-label="Select all"]')

ROWS = (By.CSS_SELECTOR, "tbody.datagrid-body tr.RaDatagrid-row")
ID_COLUMN = (By.CSS_SELECTOR, "td.column-id")
COLUMN = (By.CSS_SELECTOR, "td")
CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
