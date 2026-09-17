from pages.menu.users_page import UsersPage


def test_form_add_user(authorized_user):
    page = UsersPage(authorized_user)

    assert page.is_displayed(page.CREATE_BTN)
    page.click(page.CREATE_BTN)

    assert page.is_displayed(page.EMAIL)
    assert page.is_displayed(page.FIRST_NAME)
    assert page.is_displayed(page.LAST_NAME)
    assert page.is_displayed(page.SAVE_BTN)


def test_add_user(authorized_user):
    page = UsersPage(authorized_user)
    
    count_users = len(page.get_users())
    assert page.add_user('email@mail.ru', 'alex', 'evs')
    count_users_after_add = len(page.get_users())

    assert count_users + 1 == count_users_after_add
    

def test_add_user_with_empty_email(authorized_user):
    page = UsersPage(authorized_user)

    count_users = len(page.get_users())
    assert not page.add_user('', 'alex', 'evs')
    count_users_after_add = len(page.get_users())

    assert count_users == count_users_after_add


def test_get_users(authorized_user):
    page = UsersPage(authorized_user)
    for _ in range(23):
        page.add_user('email@mail.ru', 'alex', 'evs')

    users = page.get_users()

    assert users
    for user_id, fields in users.items():
        assert user_id
        assert fields['email']
        assert fields['first_name']
        assert fields['last_name']

    assert len(users) == 31


def test_get_user_by_id(authorized_user):
    page = UsersPage(authorized_user)
    user = page.get_user_by_id(1)

    assert user['email'] == 'john@google.com'
    assert user['first_name'] == 'John'
    assert user['last_name'] == 'Doe'


def test_get_user_by_id_not_found(authorized_user):
    page = UsersPage(authorized_user)
    user = page.get_user_by_id(1000)
    assert not user


def test_form_edit_user(authorized_user):
    page = UsersPage(authorized_user)
    user = page.get_user_by_id(1)

    email = page.get_value(page.EMAIL)
    first_name = page.get_value(page.FIRST_NAME)
    last_name = page.get_value(page.LAST_NAME)

    assert email == user['email']
    assert first_name == user['first_name']
    assert last_name == user['last_name']


def test_edit_user(authorized_user):
    page = UsersPage(authorized_user)
    user = page.get_user_by_id(1)
    page.open_users()

    assert page.edit_user(1, 'new_email@mail.ru', 'new_first_name', 'new_last_name')
    page.open_users()
    user = page.get_user_by_id(1)
    page.open_users()

    assert user['email'] == 'new_email@mail.ru'
    assert user['first_name'] == 'new_first_name'
    assert user['last_name'] == 'new_last_name'


def test_edit_with_invalid_email(authorized_user):
    page = UsersPage(authorized_user)
    user = page.get_user_by_id(1)
    email = user['email']
    page.open_users()

    assert not page.edit_user(1, '@mail.ru', 'new_first_name', 'new_last_name')
    page.open_users()
    user = page.get_user_by_id(1)
    page.open_users()

    assert user['email'] == email


def test_delete_user(authorized_user):
    page = UsersPage(authorized_user)
    assert page.delete_row(1)
    user = page.get_user_by_id(1)
    assert not user


def test_delete_all_users(authorized_user):
    page = UsersPage(authorized_user)
    page.delete_all_rows()
    users = page.get_users()
    assert len(users) == 0