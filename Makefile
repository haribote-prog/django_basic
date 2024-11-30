lint:
	poetry run flake8 .
	poetry run isort --check .
	poetry run black --check .

format:
	poetry run isort .
	poetry run black .

run:
	set -a && . ./local.env && set +a && poetry run python basic/manage.py runserver

migrate:
	set -a && . ./local.env && set +a && poetry run python basic/manage.py makemigrations
	set -a && . ./local.env && set +a && poetry run python basic/manage.py migrate

lab:
	poetry run jupyter-lab --no-browser
