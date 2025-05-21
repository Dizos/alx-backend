#!/bin/bash
echo '
ALX Backend Project - Internationalization (i18n)
Description
This project sets up a basic Flask web application as part of the ALX backend curriculum, focusing on internationalization (i18n). The initial implementation includes a single route (/) that renders a simple HTML page with a title "Welcome to ALX" and a header "Hello world".
Requirements

Python 3.7 (interpreted on Ubuntu 18.04 LTS)
pycodestyle 2.5 for style checking
Flask (install via pip install flask)
All files are executable and include proper documentation and type annotations

Repository

GitHub repository: alx-backend
Directory: 0x02-i18n

Files

0-app.py: Flask application with a single / route that renders the 0-index.html template.
templates/0-index.html: HTML template displaying "Welcome to ALX" as the page title and "Hello world" as an <h1> header.
README.md: Project documentation (this file).

Installation

Clone the repository:git clone https://github.com/<your-username>/alx-backend.git
cd alx-backend/0x02-i18n


Install dependencies:pip install flask


Ensure Python files are executable:chmod +x 0-app.py



Usage
Run the Flask application:
./0-app.py

Access the app at http://0.0.0.0:5000/ in a web browser to see the rendered page.
Documentation
All modules, classes, and functions include detailed docstrings accessible via Python's help system. For example:
import 0-app
print(0-app.__doc__)
print(0-app.index.__doc__)

'
