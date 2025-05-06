# mia_template_service_name_placeholder

## Local development

### Prerequisites
- pyenv correctly installed and configured

### Setup
- upgrade `pip`:
```
pip install --upgrade pip
```
- install `pipenv`
```
pip install pipenv
```
- install dependencies and create venv
```
pipenv sync
```
- You can now launch a shell in the created venv, with all dependencies installed:
```
pipenv shell
```

### Launching the service
First, launch a shell with the project venv. Then, you can start the service, with:
```
python -m src.app
```

### Testing
First, launch a shell with the project venv. Then, you can install the testing dependencies with:
```
pipenv sync --dev
```

Then, you can run the tests with:
```
python -m pytest tests
```