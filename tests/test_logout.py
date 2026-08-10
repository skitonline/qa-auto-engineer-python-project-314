from pages.login_page import LoginPage
from pages.administration_page import AdministrationPage


def test_logout(driver, base_url):
    login_page = LoginPage(driver)
    admin_page = AdministrationPage(driver)

    login_page.open(base_url)
    login_page.login("user", "password")

    admin_page.logout()