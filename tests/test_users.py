import pages.locators.list_structure_locators as list_loc
import pages.locators.users_locators as users_loc


def test_edit_form(users_page):
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
    assert user['email'] == "test@test.com"
    assert user['first_name'] == "Test"
    assert user['last_name'] == "Test"


def test_check_all_users(users_page):
    COUNT_USERS_IN_TABLE = 8
    users = users_page.get_all_users()
    assert COUNT_USERS_IN_TABLE == len(users)
    for id in users:
        assert users[id]['email']
        assert users[id]["first_name"]
        assert users[id]['last_name']