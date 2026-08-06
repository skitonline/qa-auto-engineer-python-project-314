from selenium.webdriver.common.by import By


def test_main_page(driver, base_url):
    driver.get(base_url)

    assert driver.title == 'Task manager'
    assert driver.find_element(By.CSS_SELECTOR, '[autocomplete="username"]')
    assert driver.find_element(By.CSS_SELECTOR, '[autocomplete="current-password"]')
    assert driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')