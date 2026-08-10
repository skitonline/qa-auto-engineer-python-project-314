from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdministrationPage(BasePage):
    PROFILE = (By.CSS_SELECTOR, 'button[aria-label="Profile"]')
    LOGOUT_TEXT = (By.XPATH, '//span[normalize-space()="Logout"]')

    def logout(self):
        self.click(self.PROFILE)
        
        logout_span = self.wait.until(EC.presence_of_element_located(self.LOGOUT_TEXT))
        self.wait.until(lambda d: logout_span.size['height'] > 0)
        parent_li = logout_span.find_element(By.XPATH, './ancestor::li[1]')
        self.click(parent_li)
