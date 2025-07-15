# Background
sok-ha is a Home Assistant custom integration written in Python. Its purpose is to connect to SOK LiFePO4 batteries over Bluetooth low energy and send and receive data. sok-ha is the Home Assistant integration – it handles scanning for devices and managing the devices and associated data in Home Assistant. sok-ha itself uses the [sok-ble library](https://github.com/IAmTheMitchell/sok-ble) to handle the Bluetooth low energy communication with the batteries. sok-ble actually sends, receives, and parses the data from the batteries. sok-ble is a separate Python package that can be used independently of sok-ha and is not included in the sok-ha repository.

# Documentation
- Use Markdown for all documentation

# Python
- Use uv to manage Python and all python packages
- Use 'uv add [package_name]' instead of 'uv pip install [package_name]'

# Testing
- Use pytest for Python testing
- Ensure all code is formatted and linted with Ruff

# Files
- Do not create binary files, such as Lambda zip files.
- Do not modify CHANGELOG.md. This is handled by CI.

# Commits
- Use conventional commits for all changes 
    - Prefix all commit messages with fix:; feat:; build:; chore:; ci:; docs:; style:; refactor:; perf:; or test: as appropriate.