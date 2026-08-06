from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def open(self, url):
        self.driver.get(url)


    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()


    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)


    def text_of(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text