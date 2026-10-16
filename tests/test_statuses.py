import pages.locators.list_structure_locators as list_loc
import pages.locators.statuses_locators as statuses_loc


COUNT_STATUSES_IN_TABLE = 5


def test_form_create(statuses_page):
    assert statuses_page.click(list_loc.CREATE_BUTTON)
    assert statuses_page.is_visibility(statuses_loc.NAME_INPUT)
    assert statuses_page.is_visibility(statuses_loc.SLUG_INPUT)


def test_add_correct_status(statuses_page):
    assert statuses_page.add_status("name", "slug")


def test_add_status_with_invalid_name(statuses_page):
    assert not statuses_page.add_status("", "slug")


def test_add_status_with_invalid_slug(statuses_page):
    assert not statuses_page.add_status("name", "")


def test_added_status_in_table(statuses_page):
    name = "name"
    slug = "slug"
    id = statuses_page.add_status(name, slug)

    status = statuses_page.get_status_by_id(id)
    assert status['name'] == name
    assert status['slug'] == slug


def test_check_all_statuses(statuses_page):
    statuses = statuses_page.get_all_statuses()
    assert COUNT_STATUSES_IN_TABLE == len(statuses)
    for id in statuses:
        assert statuses[id]['name']
        assert statuses[id]["slug"]


def test_form_edit(statuses_page):
    status = statuses_page.get_status_by_id('1')
    statuses_page.open_element_by_id('1')

    assert status['name'] == statuses_page.get_value(
        statuses_loc.NAME_INPUT
    )
    assert status['slug'] == statuses_page.get_value(
        statuses_loc.SLUG_INPUT
    )


def test_edit_status_success(statuses_page):
    id = '1'
    name = 'test'
    slug = 'test'
    assert statuses_page.edit_status(id, name, slug)

    edit_status = statuses_page.get_status_by_id(id)
    assert edit_status['id'] == id
    assert edit_status['name'] == name
    assert edit_status['slug'] == slug


def test_edit_status_with_invalid_id(statuses_page):
    assert not statuses_page.edit_status('228')


def test_delete_some_statuses(statuses_page):
    assert statuses_page.get_status_by_id('1')
    assert statuses_page.get_status_by_id('2')
    statuses_page.delete_some_rows('1', '2')

    assert not statuses_page.get_status_by_id('1')
    assert not statuses_page.get_status_by_id('2')


def test_delete_all_statuses(statuses_page):
    assert statuses_page.get_all_statuses()
    statuses_page.delete_all()
    assert not statuses_page.get_all_statuses()