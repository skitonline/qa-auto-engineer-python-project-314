from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)

    def type(self, locator, value):
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            el.click()
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