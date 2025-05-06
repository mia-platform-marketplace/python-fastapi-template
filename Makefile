setup:
	pip install pipenv
	export VENV_HOME_DIR=$(pipenv --venv)
	source $$VENV_HOME_DIR/bin/activate

start:
	python -m src.app

test:
	pipenv install --dev
	python -m pytest tests
