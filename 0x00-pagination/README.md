#!/bin/bash
echo '
# Baby Names Project

## Overview
This project processes and analyzes data from the `Popular_Baby_Names.csv` file to provide insights into baby name trends. It is written in Python 3.7 and adheres to strict coding standards, including pycodestyle 2.5.* and type annotations.

## Requirements
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle 2.5.*
- `Popular_Baby_Names.csv` file in the project root

## Setup
1. Ensure Python 3.7 is installed: `python3 --version`
2. Install pycodestyle: `pip install pycodestyle==2.5.*`
3. Place `Popular_Baby_Names.csv` in the project root.
4. Run the main script: `python3 main.py`

## Files
- `main.py`: Entry point for the project, orchestrates data processing.
- `baby_names.py`: Module containing functions to process baby names data.
- `Popular_Baby_Names.csv`: Dataset containing baby names information.

## Usage
Run `python3 main.py` to execute the program. Modify `main.py` to call specific functions from `baby_names.py` as needed.

## Notes
- All files are type-annotated and documented.
- Code adheres to pycodestyle 2.5.* standards.
- Each file ends with a newline and starts with `#!/usr/bin/env python3.'
