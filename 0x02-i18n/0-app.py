#!/usr/bin/env python3
"""
Flask application module for serving a basic webpage.

This module sets up a Flask web server with a single route to render
an index page with a welcome message.
"""

from flask import Flask, render_template
from typing import Any

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
