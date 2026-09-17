from pages.menu.labels_page import LabelsPage

def test_form_add_label(authorized_user):
    page = LabelsPage(authorized_user)

    assert page.is_displayed(page.CREATE_BTN)
    page.click(page.CREATE_BTN)

    assert page.is_displayed(page.NAME)
    assert page.is_displayed(page.SAVE_BTN)

def test_add_label(authorized_user):
    page = LabelsPage(authorized_user)

    count_labels = len(page.get_labels())
    assert page.add_label('Test Label')

    count_labels_after_add = len(page.get_labels())
    assert count_labels + 1 == count_labels_after_add

def test_add_label_with_empty_name(authorized_user):
    page = LabelsPage(authorized_user)

    count_labels = len(page.get_labels())
    assert not page.add_label('')
    page.open_labels()
    count_labels_after_add = len(page.get_labels())
    assert count_labels == count_labels_after_add

def test_get_labels(authorized_user):  
    page = LabelsPage(authorized_user)

    for _ in range(23):
        page.add_label('Test Label')

    labels = page.get_labels()
    for label_id, fields in labels.items():
        assert label_id
        assert fields['name']

    assert len(labels) == 28

def test_get_label_by_id(authorized_user):
    page = LabelsPage(authorized_user)

    label = page.get_label_by_id(1)
    assert label['name'] == 'bug'

def test_get_label_by_id_not_found(authorized_user):
    page = LabelsPage(authorized_user)
    label = page.get_label_by_id(1000)
    assert not label

def test_form_edit_label(authorized_user):
    page = LabelsPage(authorized_user)
    label = page.get_label_by_id(1)
    name = page.get_value(page.NAME)
    assert name == label['name']

def test_edit_label(authorized_user):
    page = LabelsPage(authorized_user)
    assert page.edit_label(1, 'Test Label')
    label = page.get_label_by_id(1)
    assert label['name'] == 'Test Label'

def test_edit_label_with_empty_name(authorized_user):
    page = LabelsPage(authorized_user)
    label = page.get_label_by_id(1)
    name = label['name']
    assert not page.edit_label(1, '')
    page.open_labels()
    label = page.get_label_by_id(1)
    assert label['name'] == name

def test_delete_label(authorized_user):
    page = LabelsPage(authorized_user)
    assert page.delete_row(1)
    label = page.get_label_by_id(1)
    assert not label

def test_delete_all_labels(authorized_user):
    page = LabelsPage(authorized_user)
    page.delete_all_rows()
    labels = page.get_labels()
    assert len(labels) == 0
