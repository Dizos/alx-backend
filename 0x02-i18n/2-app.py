#!/usr/bin/env python3
"""
Flask application module with internationalization support using Flask-Babel.

This module sets up a Flask web server with a single route to render an index page,
configured with Babel for language and timezone support, and includes a locale
selector to determine the best language match based on client preferences.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Any, Optional

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

@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determines the best match for supported languages based on client preferences.

    Uses request.accept_languages to select the best language from the configured
    LANGUAGES list.

    Returns:
        Optional[str]: The best matching language code (e.g., 'en' or 'fr'),
                       or None if no match is found.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
