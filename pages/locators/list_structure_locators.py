from selenium.webdriver.common.by import By

CREATE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="Create"]')
SAVE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Save"]')
DELETE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Delete"]')
SELECT_ALL = (By.CSS_SELECTOR, 'input[type="checkbox"][aria-label="Select all"]')

ROWS = (By.CSS_SELECTOR, "tbody.datagrid-body tr.RaDatagrid-row")
CELLS = (By.CSS_SELECTOR, "td.RaDatagrid-rowCell")
SPAN = (By.CSS_SELECTOR, "span.MuiTypography-root")
ID_COLUMN = (By.CSS_SELECTOR, "td.column-id")
COLUMN = (By.CSS_SELECTOR, "td")
