from pages.menu.users_page import UsersPage
from selenium.webdriver.common.by import By


def test_form_add_user(authorized_user):
    page = UsersPage(authorized_user)
    page.open_users()

    assert page.is_displayed(page.CREATE)
    page.click(page.CREATE)

    assert page.is_displayed(page.EMAIL)
    assert page.is_displayed(page.FIRST_NAME)
    assert page.is_displayed(page.LAST_NAME)
    assert page.is_displayed(page.SAVE_BUTTON)


def test_add_user(authorized_user):
    page = UsersPage(authorized_user)
    page.open_users()
    
    COUNT_LOCATOR = (By.CSS_SELECTOR, '#main-content p.MuiTablePagination-displayedRows')
    count_users = page.text_of(COUNT_LOCATOR)
    assert page.add_user('email@mail.ru', 'alex', 'evs')
    
    page.open_users()
    count_users_after_add = page.text_of(COUNT_LOCATOR)
    #не очень очевидно, но тут я выдергиваю кол-во всех пользователей из строки вида '1-8 of 10'
    assert int(count_users.split("of")[1]) + 1 == int(count_users_after_add.split("of")[1])
    


def test_add_user_with_empty_email(authorized_user):
    page = UsersPage(authorized_user)
    page.open_users()

    COUNT_LOCATOR = (By.CSS_SELECTOR, '#main-content p.MuiTablePagination-displayedRows')
    count_users = page.text_of(COUNT_LOCATOR)
    assert not page.add_user('', 'alex', 'evs')
    print(count_users)

    page.open_users()
    count_users_after_add = page.text_of(COUNT_LOCATOR)
    assert count_users == count_users_after_add