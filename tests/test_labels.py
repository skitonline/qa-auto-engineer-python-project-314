import pages.locators.labels_locators as labels_loc
import pages.locators.list_structure_locators as list_loc


def test_edit_form(labels_page):
    assert labels_page.click(list_loc.CREATE_BUTTON)
    assert labels_page.is_visibility(labels_loc.NAME_INPUT)


def test_add_correct_label(labels_page):
    assert labels_page.add_label("name")


def test_add_label_with_invalid_name(labels_page):
    assert not labels_page.add_label("")