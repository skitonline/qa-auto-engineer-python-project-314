from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)

    def _resource_list_url(self):
        base, _, fragment = self.url().partition("#")
        sections = [s for s in fragment.split("?")[0].split("/") if s]
        if sections and sections[-1].isdigit():
            sections = sections[:-1]
        return f"{base}#{'/'.join(sections)}"

    def type(self, locator, value):
        if value == '':
            return True
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            el.click()
            el.send_keys(Keys.CONTROL, "a")
            el.send_keys(value)
            return True
        except Exception:
            return False

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            return True
        except Exception:
            return False

    def is_visibility(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_value(self, locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).get_attribute('value')
        except Exception:
            return False

    def get_text(self, locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).text
        except Exception:
            return False

    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception:
            return None

    def wait_for_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except Exception:
            return []

    def wait_url_not_contains(self, substring):
        def url_does_not_contain(driver, value=substring):
            return value not in driver.current_url

        try:
            self.wait.until(url_does_not_contain)
            return True
        except Exception:
            return False

    def _wait_undo_window_closed(self):
        undo_locator = (By.XPATH, "//*[normalize-space(text()) = 'Undo']")
        try:
            self.wait.until(EC.visibility_of_element_located(undo_locator))
        except Exception:
            return
        try:
            self.wait.until(EC.invisibility_of_element_located(undo_locator))
        except Exception:
            pass
