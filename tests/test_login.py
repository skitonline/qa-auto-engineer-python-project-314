from pages.login_page import LoginPage


def test_login_fail(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)
    page.login("user", "password")
    assert page.text_of(page.WELCOME) == 'Welcome to the administration'