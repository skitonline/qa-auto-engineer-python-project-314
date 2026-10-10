def test_add_correct_user(user_page):
    assert user_page.add_user("test@test.com", "Test", "User")


def test_add_user_with_invalid_email(user_page):
    assert not user_page.add_user("test", "Test", "User")


def test_add_user_with_invalid_first_name(user_page):
    assert not user_page.add_user("test@test.com", "", "User")


def test_add_user_with_invalid_last_name(user_page):
    assert not user_page.add_user("test@test.com", "Test", "")