import pages.locators.list_structure_locators as list_loc
import pages.locators.statuses_locators as statuses_loc


def test_edit_form(statuses_page):
    assert statuses_page.click(list_loc.CREATE_BUTTON)
    assert statuses_page.is_visibility(statuses_loc.NAME_INPUT)
    assert statuses_page.is_visibility(statuses_loc.SLUG_INPUT)