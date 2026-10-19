import pages.locators.list_structure_locators as list_loc
import pages.locators.tasks_locators as tasks_loc

STATUS = "Draft"
TARGET_STATUS = "Published"
ASSIGNEE = "john@google.com"
OTHER_ASSIGNEE = "sarah@example.com"
LABEL = "bug"
OTHER_LABEL = "feature"
COUNT_TASKS = 15


def test_form_create(tasks_page):
    assert tasks_page.click(list_loc.CREATE_BUTTON)
    assert tasks_page.is_visibility(tasks_loc.ASSIGNEE_SELECT)
    assert tasks_page.is_visibility(tasks_loc.TITLE_INPUT)
    assert tasks_page.is_visibility(tasks_loc.CONTENT_INPUT)
    assert tasks_page.is_visibility(tasks_loc.STATUS_SELECT)
    assert tasks_page.is_visibility(tasks_loc.LABEL_SELECT)


def test_add_correct_task(tasks_page):
    assert tasks_page.add_task(ASSIGNEE, 'title', STATUS)


def test_add_task_with_invalid_data(tasks_page):
    assert not tasks_page.add_task("wrong", "title", STATUS)


def test_added_task(tasks_page):
    title = "title"
    content = "content"
    task_id = tasks_page.add_task(assignee=ASSIGNEE,
        title=title, status=STATUS, content=content, label=LABEL)

    task = tasks_page.get_task_info(task_id)

    assert task['assignee'] == ASSIGNEE
    assert task['title'] == title
    assert task['content'] == content
    assert task['status'] == STATUS
    assert task['label'] == LABEL


def test_check_all_tasks(tasks_page):
    tasks = tasks_page.get_all_tasks()
    assert tasks
    for task_id in tasks:
        assert tasks[task_id]['title']
        assert tasks[task_id]['status']


def test_filtered_by_status(tasks_page):
    title = "title"
    assert tasks_page.add_task(ASSIGNEE, title, STATUS)
    assert tasks_page.filter_by_status(STATUS)

    cards = tasks_page.get_cards_in_column(STATUS)
    assert any(title in card for card in cards)
    assert not tasks_page.get_cards_in_column(TARGET_STATUS)


def test_filtered_by_assignee(tasks_page):
    tasks_page.add_task(ASSIGNEE, "title_john", STATUS, )
    tasks_page.add_task(OTHER_ASSIGNEE, "title_sarah", STATUS)

    assert tasks_page.filter_by_assignee(ASSIGNEE)

    tasks = tasks_page.get_all_tasks()
    titles = [task['title'] for task in tasks.values()]
    assert "title_john" in titles
    assert "title_sarah" not in titles


def test_filtered_by_label(tasks_page):
    tasks_page.add_task(ASSIGNEE, "title_bug", STATUS, label=LABEL)
    tasks_page.add_task(ASSIGNEE, "title_feature", STATUS, label=OTHER_LABEL)

    assert tasks_page.filter_by_label(LABEL)

    tasks = tasks_page.get_all_tasks()
    titles = [task['title'] for task in tasks.values()]
    assert "title_bug" in titles
    assert "title_feature" not in titles


def test_edit_task(tasks_page):
    task_id = tasks_page.add_task(ASSIGNEE, "title", STATUS)
    new_title = "edit_title"
    assert tasks_page.edit_task(task_id, title=new_title, status=TARGET_STATUS)

    task = tasks_page.get_task_info(task_id)
    assert task['assignee'] == ASSIGNEE
    assert task['title'] == new_title
    assert task['status'] == TARGET_STATUS


def test_move_card(tasks_page):
    title = "title"
    task_id = tasks_page.add_task(ASSIGNEE, title, STATUS)

    assert tasks_page.move_card(task_id, TARGET_STATUS)

    cards = tasks_page.get_cards_in_column(TARGET_STATUS)
    assert any(title in card for card in cards)


def test_delete_task(tasks_page):
    title = "title"
    task_id = tasks_page.add_task(ASSIGNEE, title, STATUS)

    assert tasks_page.delete_task(task_id)
    assert not tasks_page.get_task_by_id(task_id)

    tasks = tasks_page.get_all_tasks()
    titles = [task['title'] for task in tasks.values()]
    assert title not in titles
