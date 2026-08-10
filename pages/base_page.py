from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, 'div.RaNotification-error')

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def open(self, url):
        self.driver.get(url)


    def wait_for_notification_to_disappear(self):
            self.wait.until(EC.invisibility_of_element_located(self.ERROR_NOTIFICATION))


    def click(self, locator):
        self.wait_for_notification_to_disappear()
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()


    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)


    def text_of(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text