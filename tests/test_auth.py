from pages.interface_page import InterfacePage
from pages.login_page import LoginPage


def test_login_success(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)

    assert page.login('user', 'password')
    assert 'login' not in page.url()


def test_login_with_invalid_login(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)

    assert not page.login('', 'password')
    assert 'login' in page.url()


def test_login_with_invalid_password(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)

    assert not page.login('user', '')
    assert 'login' in page.url()


def test_logout(authorized_user):
    page = InterfacePage(authorized_user)

    assert page.logout()
    assert '/login' in page.url()