from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def open(self, url):
        self.driver.get(url)


    def url(self):
        return self.driver.current_url


    def is_displayed(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False


    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            return True
        except Exception:
            return False


    def text_of(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    
    def get_value(self, locator, attribute='value'):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.get_attribute(attribute)


    def fill_field(self, locator, value):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.click()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(value)




    