.PHONY: test lint

test:
	pytest -q

lint:
	flake8 src
