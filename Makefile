.PHONY: all install run format lint type_check test 


all: format lint type_check test 

install:
	poetry install

run:
	poetry run python main.py

format:
	poetry run ruff format

lint:
	poetry run ruff check --fix

type_check:
	poetry run mypy .

test:
	poetry run pytest .
