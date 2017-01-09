# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = 'Multiple'
SITENAME = 'Nairobi GNU/Linux Users Group'
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

# http://docs.getpelican.com/en/stable/plugins.html#how-to-use-plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

# Theme settings --------------------------------------------------------------

THEME = 'themes/pelican-alchemy/alchemy'

SITESUBTITLE = 'A lively community of GNU/Linux enthusiasts'
SITEIMAGE = '/images/profile.png'
DESCRIPTION = 'A not-for-profit community serving the greater Nairobi area. ' \
              'We are a collection of people dedicated to GNU/Linux, Free ' \
              'Software, Open Source, and related topics.'

LINKS = (
    ('IRC', 'https://webchat.freenode.net/?channels=nairobilug'),
)

ICONS = [
    ('github', 'http://github.com/nairobilug'),
    ('twitter', 'http://twitter.com/nairobilug'),
]

PYGMENTS_STYLE = 'monokai'
RFG_FAVICONS = True

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
