# Create the virtual environment.
make venv-dev
# Install the pre-commit hooks.
.venv/bin/pre-commit run --all-files
