from pages.login_page import LoginPage


def test_login_success(driver, base_url):
    page = LoginPage(driver)

    page.open(base_url)
    login = page.login('user', 'password')

    assert login
    assert 'login' not in page.url()


def test_login_with_invalid_login(driver, base_url):
    page = LoginPage(driver)

    page.open(base_url)
    login = page.login('', 'password')

    assert not login
    assert 'login' in page.url()


def test_login_with_invalid_password(driver, base_url):
    page = LoginPage(driver)

    page.open(base_url)
    login = page.login('user', '')
    
    assert not login
    assert 'login' in page.url()