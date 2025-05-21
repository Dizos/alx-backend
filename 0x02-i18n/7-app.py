#!/usr/bin/env python3
"""
Flask application module with internationalization and mock user login support.

This module sets up a Flask web server with a single route to render an index page,
configured with Babel for language and timezone support, a locale selector that
prioritizes URL parameters, user settings, and client preferences, a timezone
selector with similar logic, and a mock user login system using a 'login_as' query
parameter to set flask.g.user.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from typing import Any, Optional, Dict

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Optional[Dict[str, Any]]:
    """
    Retrieves a user dictionary based on the 'login_as' query parameter.

    Returns:
        Optional[Dict[str, Any]]: The user dictionary if found, else None.
    """
    try:
        user_id = int(request.args.get('login_as', ''))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None

@app.before_request
def before_request() -> None:
    """
    Executes before each request to set flask.g.user based on the 'login_as' parameter.

    Uses get_user to retrieve the user and stores it in flask.g.user.
    """
    g.user = get_user()

@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determines the best match for supported languages based on query parameter,
    user settings, or client preferences.

    Priority order:
    1. 'locale' query parameter, if valid.
    2. User's preferred locale from user settings, if valid.
    3. Best match from request.accept_languages.
    4. Default locale from BABEL_DEFAULT_LOCALE.

    Returns:
        Optional[str]: The selected language code (e.g., 'en' or 'fr'),
                       or None if no match is found.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the timezone based on query parameter, user settings, or default.

    Priority order:
    1. 'timezone' query parameter, if valid.
    2. User's preferred timezone from user settings, if valid.
    3. Default timezone from BABEL_DEFAULT_TIMEZONE ('UTC').

    Validates timezones using pytz.timezone, catching UnknownTimeZoneError.

    Returns:
        str: The selected timezone (e.g., 'UTC', 'Europe/Paris').
    """
    # Check URL parameter
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Check user settings
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def index() -> str:
    """
    Renders the index page with translated title, header, and login message.

    Uses _() to translate message IDs 'home_title', 'home_header', 'logged_in_as',
    and 'not_logged_in'. Displays a welcome message if a user is logged in.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('7-index.html',
                           home_title=_('home_title'),
                           home_header=_('home_header'),
                           login_message=_('logged_in_as', username=g.user['name']) if g.user else _('not_logged_in'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
