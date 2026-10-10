start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

install:
	uv sync

setup:
	uv sync

check:
	uv run ruff check .

fix:
	uv run ruff check --fix .

test:
	uv run pytest