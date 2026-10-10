import pages.locators.login_locators as loc


def test_smoke(driver, base_url):
    driver.get(base_url)

    assert driver.title == 'Task manager'
    assert driver.find_element(*loc.USERNAME_INPUT)
    assert driver.find_element(*loc.PASSWORD_INPUT)
    assert driver.find_element(*loc.SUBMIT_BUTTON)