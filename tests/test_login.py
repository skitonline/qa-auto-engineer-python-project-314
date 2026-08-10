from pages.login_page import LoginPage


def test_login_succes(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)
    assert page.login("user", "password")
    assert page.text_of(page.WELCOME) == 'Welcome to the administration'


def test_empty_password(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)
    assert not page.login("user", "")