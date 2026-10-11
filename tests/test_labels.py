import pages.locators.labels_locators as labels_loc
import pages.locators.list_structure_locators as list_loc


def test_edit_form(labels_page):
    assert labels_page.click(list_loc.CREATE_BUTTON)
    assert labels_page.is_visibility(labels_loc.NAME_INPUT)