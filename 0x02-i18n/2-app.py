#!/usr/bin/env python3

"""Configures Babel for multi-language support"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Babel config"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector()
def get_locale() -> str:
    """Retrieves the locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


_(u'%(home_title)s', home_title=home_title)
_(u'%(home_header)s', home_header=home_header)
@app.route('/', strict_slashes=False)
def index() -> str:
    """Renders a basic page"""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()
