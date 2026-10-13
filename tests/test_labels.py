from pages.locators.labels_locators import NAME_INPUT
from pages.locators.list_structure_locators import CREATE_BUTTON


def test_form_create(labels_page):
    assert labels_page.click(CREATE_BUTTON)
    assert labels_page.is_visibility(NAME_INPUT)


def test_add_correct_label(labels_page):
    assert labels_page.add_label("name")


def test_add_label_with_invalid_name(labels_page):
    assert not labels_page.add_label("")


def test_added_label_in_table(labels_page):
    name = "name"
    id = labels_page.add_label(name)

    label = labels_page.get_label_by_id(id)
    assert label['name'] == name


def test_check_all_labels(labels_page):
    COUNT_LABELS_IN_TABLE = 5
    labels = labels_page.get_all_labels()
    assert COUNT_LABELS_IN_TABLE == len(labels)
    for id in labels:
        assert labels[id]['name']


def test_form_edit(labels_page):
    label = labels_page.get_label_by_id('1')
    labels_page.open_element_by_id('1')
    assert label['name'] == labels_page.get_text_from_field(NAME_INPUT)


def test_edit_label_success(labels_page):
    id = '1'
    name = 'test'
    assert labels_page.edit_label(id, name)

    edit_label = labels_page.get_label_by_id(id)
    assert edit_label['id'] == id
    assert edit_label['name'] == name


def test_edit_label_with_invalid_id(labels_page):
    assert not labels_page.edit_label('9232')


def test_delete_some_labels(labels_page):
    assert labels_page.delete_some_rows('1', '2')
    assert not labels_page.get_label_by_id('1')
    assert not labels_page.get_label_by_id('2')


def test_delete_all_labels(labels_page):
    assert labels_page.get_all_labels()
    labels_page.delete_all()
    assert not labels_page.get_all_labels()