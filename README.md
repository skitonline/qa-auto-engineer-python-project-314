# Тестирование канбан-доски

[![hexlet-check](https://github.com/skitonline/qa-auto-engineer-python-project-314/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/skitonline/qa-auto-engineer-python-project-314/actions)[![CI](https://github.com/skitonline/qa-auto-engineer-python-project-314/actions/workflows/ci.yml/badge.svg)](https://github.com/skitonline/qa-auto-engineer-python-project-314/actions/workflows/ci.yml)[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=skitonline_qa-auto-engineer-python-project-314&metric=coverage)](https://sonarcloud.io/summary/new_code?id=skitonline_qa-auto-engineer-python-project-314)

UI-автотесты для приложения Task Manager (канбан-доска): Python, Selenium, pytest.
Взаимодействие со страницами оформлено по паттерну Page Object.

Покрытые разделы:

- **Аутентификация** — вход и выход, проверка загрузки дашборда
- **Пользователи** — создание с валидацией email, просмотр, редактирование, удаление
- **Статусы задач** — CRUD и массовое удаление
- **Метки** — CRUD и массовое удаление
- **Задачи** — создание, редактирование, удаление, перемещение между колонками,
  фильтры по статусу, исполнителю и метке

## Структура проекта

- **pages** Страницы сайта в формате Page Objects
- **pages/locators** Локаторы страниц
- **tests** Тесты

## Требования

- Python 3.14\+
- [uv](https://docs.astral.sh/uv/)
- Docker (для запуска тестируемого приложения)
- Google Chrome / Chromium

## Установка

```bash
make install
```

## Запуск приложения

Приложение поднимается в Docker и доступно на <http://localhost:5173>:

```bash
make start
```

## Проверить код линтером

```bash
make check
```

## Запуск тестов

```bash
make test       
```

## CI

- **hexlet-check** — служебная проверка Hexlet
- **CI** - Мой CI, который запускает контейнер сайта, проверяет линтинг и прогоняет тест 

## Настройка окружения


|Переменная|Назначение|По умолчанию|
|:---|:---|:---|
|`APP_BASE_URL`|адрес тестируемого приложения|`http://localhost:5173`|
|`LOGIN`|адрес тестируемого приложения|`test`|
|`PASSWORD`|адрес тестируемого приложения|`test`|
