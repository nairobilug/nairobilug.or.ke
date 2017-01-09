# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = 'Multiple'
SITENAME = 'Nairobi LUG'
SITEURL = ''  # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = PAGE_LANG_URL

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-256x256.png': {'path': 'android-chrome-256x256.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
}

# Theme settings --------------------------------------------------------------

THEME = 'theme/alchemy'

SITE_SUBTEXT = 'A lively community of GNU/Linux enthusiasts'
META_DESCRIPTION = 'A not-for-profit community serving the greater Nairobi ' \
                   'area. We are a collection of people dedicated to ' \
                   'GNU/Linux, Free Software, Open Source, and related topics.'

PAGES_ON_MENU = True
PROFILE_IMAGE = '/images/profile.svg width="200" height="200"'
SHOW_ARTICLE_AUTHOR = True
EXTRA_FAVICON = True

MENU_ITEMS = (
    ('IRC', 'http://webchat.freenode.net/?channels=nairobilug'),
    ('Mailing List', 'https://groups.google.com/forum/#!forum/nairobi-gnu'),
)

GITHUB_ADDRESS = 'https://github.com/nairobilug'
TWITTER_ADDRESS = 'https://twitter.com/nairobilug'
GPLUS_ADDRESS = 'https://plus.google.com/communities/107260210367217532462'
