from pages.menu.statuses_page import StatusesPage

def test_form_add_status(authorized_user):
    page = StatusesPage(authorized_user)

    assert page.is_displayed(page.CREATE_BTN)
    page.click(page.CREATE_BTN)

    assert page.is_displayed(page.NAME)
    assert page.is_displayed(page.SLUG)
    assert page.is_displayed(page.SAVE_BTN)


def test_add_status(authorized_user):
    page = StatusesPage(authorized_user)

    count_statuses = len(page.get_statuses())
    assert page.add_status('Test Status', 'test-status')
    count_statuses_after_add = len(page.get_statuses())

    assert count_statuses + 1 == count_statuses_after_add

def test_add_status_with_empty_name(authorized_user):
    page = StatusesPage(authorized_user)
    count_statuses = len(page.get_statuses())
    assert not page.add_status('', 'test-status')
    count_statuses_after_add = len(page.get_statuses())
    assert count_statuses == count_statuses_after_add

def test_get_statuses(authorized_user):
    page = StatusesPage(authorized_user)
    for _ in range(23):
        page.add_status('Test Status', 'test-status')

    statuses = page.get_statuses()
    
    assert statuses
    for status_id, fields in statuses.items():
        assert status_id
        assert fields['name']
        assert fields['slug']

def test_get_status_by_id(authorized_user):
    page = StatusesPage(authorized_user)
    status = page.get_status_by_id(1)
    assert status['name'] == 'Draft'
    assert status['slug'] == 'draft'

def test_get_status_by_id_not_found(authorized_user):
    page = StatusesPage(authorized_user)
    status = page.get_status_by_id(1000)
    assert not status

def test_form_edit_status(authorized_user):
    page = StatusesPage(authorized_user)
    status = page.get_status_by_id(1)
    name = page.get_value(page.NAME)
    slug = page.get_value(page.SLUG)

    assert name == status['name']
    assert slug == status['slug']

def test_edit_status(authorized_user):
    page = StatusesPage(authorized_user)
    assert page.edit_status(1, 'Test Status', 'test-status')
    status = page.get_status_by_id(1)
    assert status['name'] == 'Test Status'
    assert status['slug'] == 'test-status'

def test_edit_status_with_empty_name(authorized_user):
    page = StatusesPage(authorized_user)
    status = page.get_status_by_id(1)
    name = status['name']

    assert not page.edit_status(1, '', 'test-status')
    page.open_statuses()
    status = page.get_status_by_id(1)
    assert status['name'] == name

def test_delete_status(authorized_user):
    page = StatusesPage(authorized_user)
    assert page.delete_row(1)
    status = page.get_status_by_id(1)
    assert not status

def test_delete_all_statuses(authorized_user):
    page = StatusesPage(authorized_user)
    page.delete_all_rows()
    statuses = page.get_statuses()
    assert len(statuses) == 0