
from django.apps import AppConfig

from .widget import *

default_app_config = 'leonardo_cookie_law.Config'


LEONARDO_APPS = [
    'leonardo_cookie_law',
    'cookielaw'
]

LEONARDO_JS_FILES = [
    'cookielaw/js/cookielaw.js'
]

LEONARDO_CSS_FILES = [
    'cookielaw/default.css'
]

LEONARDO_OPTGROUP = 'Cookie Law'

LEONARDO_WIDGETS = [
    CookieLawWidget,
]

LEONARDO_CONFIG = {
    'SITE_INFO_URL': ('', 'URL to site information.'),
}


class Config(AppConfig):
    name = 'leonardo_cookie_law'
    verbose_name = LEONARDO_OPTGROUP
