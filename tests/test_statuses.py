import pages.locators.list_structure_locators as list_loc
import pages.locators.statuses_locators as statuses_loc


def test_edit_form(statuses_page):
    assert statuses_page.click(list_loc.CREATE_BUTTON)
    assert statuses_page.is_visibility(statuses_loc.NAME_INPUT)
    assert statuses_page.is_visibility(statuses_loc.SLUG_INPUT)


def test_add_correct_status(statuses_page):
    assert statuses_page.add_status("name", "slug")


def test_add_status_with_invalid_name(statuses_page):
    assert not statuses_page.add_status("", "slug")


def test_add_status_with_invalid_slug(statuses_page):
    assert not statuses_page.add_status("name", "")