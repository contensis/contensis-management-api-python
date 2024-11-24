.DEFAULT_GOAL:= help  # because it's is a safe task.

clean:  # Remove all build, test, coverage and Python artifacts.
	rm -rf .venv
	rm -rf *.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

http:  # Run the HTTP tests.
	httpyac send tests/http/*.http --all --quiet

lint:  # Lint the code with ruff and mypy.
	.venv/bin/python -m ruff check ./src ./tests
	.venv/bin/python -m mypy ./src ./tests
	# .venv/bin/sourcery login --token $${SOURCERY_TOKEN}
	# .venv/bin/sourcery review ./src ./tests

lock:  # Create the lock file and requirements file.
	rm -f requirements.*
	.venv/bin/python -m uv pip compile --output-file requirements.txt pyproject.toml
	.venv/bin/python -m uv pip compile --extra dev --output-file requirements.dev.txt pyproject.toml

report:  # Report the python version and pip list.
	.venv/bin/python --version
	.venv/bin/python -m pip list -v
	.venv/bin/pytest --cov=contensis_management --cov-fail-under=80

test:  # Run tests.
	.venv/bin/python -m pytest ./tests --verbose --color=yes

venv:  # Create an empty virtual environment (enough to create the requirements files).
	-python -m venv .venv  # Skip failure that happens in Github Action due to permissions.
	.venv/bin/python -m pip install --upgrade pip uv

venv-dev:  # Create the development virtual environment.
	$(MAKE) venv
	.venv/bin/python -m uv pip install -r requirements.dev.txt
	.venv/bin/python -m uv pip install --editable .

venv-prod:  # Create the production virtual environment.
	$(MAKE) venv
	.venv/bin/python -m uv pip install -r requirements.txt
	.venv/bin/python -m uv pip install --editable .
