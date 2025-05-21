#!/usr/bin/env python3
"""
Flask application module with internationalization support using Flask-Babel.

This module sets up a Flask web server with a single route to render an index page,
configured with Babel for language and timezone support.
"""

from flask import Flask, render_template
from flask_babel import Babel
from typing import Any

class Config:
    """
    Configuration class for Flask application settings.

    Defines supported languages and Babel configuration for locale and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
