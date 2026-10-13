from selenium.webdriver.common.by import By

# Поля формы создания/редактирования задачи
TITLE_INPUT = (By.CSS_SELECTOR, 'input[name="title"]')
STATUS_INPUT = (By.CSS_SELECTOR, 'input[name="status_id"]')
ASSIGNEE_INPUT = (By.CSS_SELECTOR, 'input[name="assignee_id"]')
LABEL_INPUT = (By.CSS_SELECTOR, 'input[name="label_id"]')
CONTENT_INPUT = (By.CSS_SELECTOR, 'textarea[name="content"]')

# Видимые элементы выпадающих списков (MUI Select)
STATUS_SELECT = (
    By.CSS_SELECTOR, '.ra-input-status_id [role="combobox"]'
)
ASSIGNEE_SELECT = (
    By.CSS_SELECTOR, 'div.ra-input-assignee_id [role="combobox"]'
)
LABEL_SELECT = (
    By.CSS_SELECTOR, 'div.ra-input-label_id [role="combobox"]'
)

# Выпадающие списки (MUI Select): сам список и его пункты
SELECT_COMBOBOX = (By.CSS_SELECTOR, "div[role='combobox']")
SELECT_LISTBOX = (By.CSS_SELECTOR, "[role='listbox']")
SELECT_OPTION = (By.CSS_SELECTOR, "[role='option']")
MODAL_BACKDROP = (By.CSS_SELECTOR, ".MuiBackdrop-root")

# Канбан-доска
COLUMN = (By.CSS_SELECTOR, "[data-rfd-droppable-id]")
COLUMN_HEADER = (By.XPATH, "./preceding-sibling::*[1]")
CARD = (By.CSS_SELECTOR, "[data-rfd-draggable-id]")
CARD_TITLE = (By.CSS_SELECTOR, ".MuiTypography-h5")
CARD_CONTENT = (By.CSS_SELECTOR, "p.MuiTypography-body2")
CARD_EDIT_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="Edit"]')

# Поля фильтров
STATUS_FILTER = (By.CSS_SELECTOR, 'input[name="status_id"]')
ASSIGNEE_FILTER = (By.CSS_SELECTOR, 'input[name="assignee_id"]')
LABEL_FILTER = (By.CSS_SELECTOR, 'input[name="label_id"]')