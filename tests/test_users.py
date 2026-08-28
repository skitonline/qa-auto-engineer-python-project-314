from pages.menu.users_page import UsersPage


def test_form_add_user(authorized_user):
    page = UsersPage(authorized_user)
    page.open_users()

    assert page.is_displayed(page.CREATE_BTN)
    page.click(page.CREATE_BTN)

    assert page.is_displayed(page.EMAIL)
    assert page.is_displayed(page.FIRST_NAME)
    assert page.is_displayed(page.LAST_NAME)
    assert page.is_displayed(page.SAVE_BTN)


def test_add_user(authorized_user):
    page = UsersPage(authorized_user)
    
    count_users = page.how_many_elements_countains()
    assert page.add_user('email@mail.ru', 'alex', 'evs')
    count_users_after_add = page.how_many_elements_countains()

    assert count_users + 1 == count_users_after_add
    

def test_add_user_with_empty_email(authorized_user):
    page = UsersPage(authorized_user)

    count_users = page.how_many_elements_countains()
    assert not page.add_user('', 'alex', 'evs')
    count_users_after_add = page.how_many_elements_countains()

    assert count_users == count_users_after_add


def test_get_users(authorized_user):
    page = UsersPage(authorized_user)
    for _ in range(23):
        page.add_user('email@mail.ru', 'alex', 'evs')
    users = page.get_users()

    for user in users:
        user = list(user.values())[0]
        assert user['email']
        assert user['first_name']
        assert user['last_name']
    assert len(users) == page.how_many_elements_countains()