lint:
	poetry run flake8 .
	poetry run isort --check .
	poetry run black --check .

format:
	poetry run isort .
	poetry run black .