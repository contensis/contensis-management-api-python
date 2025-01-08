.DEFAULT_GOAL:= help  # because it's is a safe task.

clean:  # Remove all build, test, coverage and Python artifacts.
	rm -rf .venv
	rm -rf *.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

http:  # Run the HTTP tests (the Contensis instance needs to be accessible for authentication).
	httpyac send tests/http/*.http --all --quiet

lint:  # Lint the code with ruff and mypy.
	.venv/bin/python -m ruff check ./src ./tests
	.venv/bin/python -m mypy ./src ./tests
	# .venv/bin/sourcery login --token $${SOURCERY_TOKEN}
	# .venv/bin/sourcery review ./src ./tests

lock:  # Create the lock file and requirements file.
	rm -f requirements.*
	uv pip compile --output-file requirements.txt pyproject.toml
	uv pip compile --extra dev --output-file requirements.dev.txt pyproject.toml

report:  # Report the python version and pip list.
	uv pip list --python .venv/bin/python
	.venv/bin/python --version
	.venv/bin/pytest --cov=contensis_management --cov-fail-under=80

test:  # Run tests.
	.venv/bin/python -m pytest ./tests --verbose --color=yes

venv:  # Create an empty virtual environment (enough to create the requirements files).
	uv venv .venv

venv-dev:  # Create the development virtual environment.
	$(MAKE) venv
	uv pip install --python .venv/bin/python --requirements requirements.dev.txt
	uv pip install --python .venv/bin/python --editable .

venv-prod:  # Create the production virtual environment.
	$(MAKE) venv
	uv pip install --python .venv/bin/python --requirements requirements.txt
	uv pip install --python .venv/bin/python --editable .
