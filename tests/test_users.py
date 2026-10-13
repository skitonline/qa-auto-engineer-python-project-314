import pages.locators.list_structure_locators as list_loc
import pages.locators.users_locators as users_loc


def test_form_create(users_page):
    assert users_page.click(list_loc.CREATE_BUTTON)
    assert users_page.is_visibility(users_loc.EMAIL_INPUT)
    assert users_page.is_visibility(users_loc.FIRST_NAME_INPUT)
    assert users_page.is_visibility(users_loc.LAST_NAME_INPUT)


def test_add_correct_user(users_page):
    assert users_page.add_user("test@test.com", "Test", "User")


def test_add_user_with_invalid_email(users_page):
    assert not users_page.add_user("test", "Test", "User")


def test_add_user_with_invalid_first_name(users_page):
    assert not users_page.add_user("test@test.com", "", "User")


def test_add_user_with_invalid_last_name(users_page):
    assert not users_page.add_user("test@test.com", "Test", "")


def test_added_user_in_table(users_page):
    email = "test@test.com"
    first_name = "Test"
    last_name = "Test"
    id = users_page.add_user(email, first_name, last_name)

    user = users_page.get_user_by_id(id)
    assert user['email'] == email
    assert user['first_name'] == first_name
    assert user['last_name'] == last_name


def test_check_all_users(users_page):
    COUNT_USERS_IN_TABLE = 8
    users = users_page.get_all_users()
    assert COUNT_USERS_IN_TABLE == len(users)
    for id in users:
        assert users[id]['email']
        assert users[id]["first_name"]
        assert users[id]['last_name']


def test_form_edit(users_page):
    user = users_page.get_user_by_id('1')
    users_page.open_element_by_id('1')
    assert user['email'] == users_page.get_text_from_field(
        users_loc.EMAIL_INPUT
    )
    assert user['first_name'] == users_page.get_text_from_field(
        users_loc.FIRST_NAME_INPUT
    )
    assert user['last_name'] == users_page.get_text_from_field(
        users_loc.LAST_NAME_INPUT
    )


def test_edit_user_success(users_page):
    id = '1'
    email = 'new@email.ru'
    first_name = 'first'
    last_name = 'last'
    assert users_page.edit_user(id, email, first_name, last_name)

    edit_user = users_page.get_user_by_id(id)
    assert edit_user['id'] == id
    assert edit_user['email'] == email
    assert edit_user['first_name'] == first_name
    assert edit_user['last_name'] == last_name


def test_edit_user_with_invalid_id(users_page):
    assert not users_page.edit_user('9999')


def test_edit_user_with_invalid_email(users_page):
    assert not users_page.edit_user('1', '@')


def test_delete_some_users(users_page):
    assert users_page.delete_user('1', '2')
    assert not users_page.get_user_by_id('1')
    assert not users_page.get_user_by_id('2')


def test_delete_all_users(users_page):
    assert users_page.get_all_users()
    users_page.delete_all()
    assert not users_page.get_all_users()