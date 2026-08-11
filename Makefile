.PHONY: start test

install:
	uv sync --no-dev
start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

test:
	uv run pytest