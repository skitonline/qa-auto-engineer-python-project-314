from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_login_success(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)
    assert page.login("user", "password")
    assert 'login' not in page.url()


def test_login_with_empty_password(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)
    assert not page.login("user", "")
    assert 'login' in page.url()


def test_logout(authorized_user):
    page = MainPage(authorized_user)
    page.logout()
    assert '/login' in page.url()