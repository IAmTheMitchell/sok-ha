# Background

sok-ha is a Home Assistant custom integration written in Python and distributed via HACS. Its purpose is to connect to SOK LiFePO4 batteries over Bluetooth low energy and send and receive data. sok-ha is the Home Assistant integration – it handles scanning for devices and managing the devices and associated data in Home Assistant. sok-ha itself uses the [sok-ble library](https://github.com/IAmTheMitchell/sok-ble) to handle the Bluetooth low energy communication with the batteries. sok-ble actually sends, receives, and parses the data from the batteries. sok-ble is a separate Python package that can be used independently of sok-ha and is not included in the sok-ha repository.

# Documentation

- Use Markdown for all documentation.
- Place documentation in the `docs/` directory.

# Code Style

- Add comments to code when it may be unclear what the code does or how it functions.
- Comments should be full sentences and end with a period.
- Maintainable and understandable code is preferred over complex code.

# Python

- Use uv to manage Python and all Python packages.
- Use 'uv add [package_name]' instead of 'uv pip install [package_name]'.

# Testing

- Use pytest for Python testing.
- Ensure all code is formatted and linted with Ruff.

# Files

- Do not create binary files, such as Lambda zip files.
- Do not modify CHANGELOG.md. This is handled by CI.

# Commits

- Use conventional commits for all changes
  - Prefix all commit messages with fix:; feat:; build:; chore:; ci:; docs:; style:; refactor:; perf:; or test: as appropriate.

# Before Checking In Code

- Fix all code formatting and quality issues in the entire codebase.
- Ensure all new code is covered by appropriate unit tests.

## Python

Fix all Python formatting and linting issues.

### Steps:

1. **Format with ruff**: `uv run ruff format .`
2. **Lint with ruff**: `uv run ruff check . --output-format=github`
3. **Type check with ty**: `uv run ty check . --output-format=github`
4. **Run unit tests**: `uv run pytest tests`

## General Process:

1. Run automated formatters first.
2. Fix remaining linting issues manually.
3. Resolve type checking errors.
4. Verify all tests pass with no errors.
5. Review changes before committing.

## Common Issues:

- Import order conflicts between tools
- Line length violations
- Unused imports/variables
- Type annotation requirements
- Missing return types
- Inconsistent quotes/semicolons
