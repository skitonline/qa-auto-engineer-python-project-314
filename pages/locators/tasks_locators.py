from selenium.webdriver.common.by import By

ASSIGNEE_SELECT = (By.XPATH,
        '//input[@name="assignee_id"]/preceding-sibling::div[@role="combobox"]')
TITLE_INPUT = (By.CSS_SELECTOR, 'input[name="title"]')
CONTENT_INPUT = (By.CSS_SELECTOR, 'textarea[name="content"]')
STATUS_SELECT = (By.XPATH,
        '//input[@name="status_id"]/preceding-sibling::div[@role="combobox"]')
LABEL_SELECT = (By.XPATH,
        '//input[@name="label_id"]/preceding-sibling::div[@role="combobox"]')

BACKDROP = (By.CSS_SELECTOR, ".MuiBackdrop-root")

COLUMN = (By.CSS_SELECTOR, "[data-rfd-droppable-id]")
COLUMN_HEADER = (By.XPATH, "./preceding-sibling::*[1]")
CARD = (By.CSS_SELECTOR, "[data-rfd-draggable-id]")
CARD_TITLE = (By.CSS_SELECTOR, ".MuiTypography-h5")
CARD_CONTENT = (By.CSS_SELECTOR, "p.MuiTypography-body2")
