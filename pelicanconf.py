from __future__ import unicode_literals


# Pelican settings ------------------------------------------------------------

# Basic
SITENAME = 'Nairobi LUG'
SITEURL = 'https://nairobilug.or.ke'

AUTHOR = 'Multiple'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
THEME = 'theme/alchemy'
TIMEZONE = 'Africa/Nairobi'

# Plugins
# See: http://docs.getpelican.com/en/latest/plugins.html
PLUGINS = ['sitemap']

# Set to True when testing locally
RELATIVE_URLS = False

# Feeds
FEED_ATOM = 'feed/atom.xml'
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# URLs
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'

# Delete the output directory, before generating new files
DELETE_OUTPUT_DIRECTORY = True

# The static paths you want to have accessible on the output path "static"
STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/favicon.ico',
    'extra/favicon-16x16.png',
    'extra/favicon-32x32.png',
    'extra/favicon-96x96.png',
    'extra/favicon-160x160.png',
    'extra/favicon-196x196.png',
    'extra/robots.txt',
]

# Extra metadata dictionaries keyed by relative path
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'extra/favicon-160x160.png': {'path': 'favicon-160x160.png'},
    'extra/favicon-196x196.png': {'path': 'favicon-196x196.png'},
    'extra/robots.txt': {'path': 'robots.txt'},
}


# Theme settings --------------------------------------------------------------

PAGES_ON_MENU = True
PROFILE_IMAGE = '/images/profile.svg width="200" height="200"'
SHOW_ARTICLE_AUTHOR = True
SITE_SUBTEXT = 'Nairobi GNU/Linux Users Group'
META_DESCRIPTION = '''Nairobi GNU/Linux Users Group is a not-for-profit
                   community serving the greater Nairobi area. We are a
                   collection of people dedicated to GNU/Linux, Free Software,
                   Open Source, and other related topics.'''

EXTRA_FAVICON = True

# LICENSE_URL = ''
# LICENSE_NAME = ''

MENU_ITEMS = (
    ('IRC', 'https://kiwiirc.com/client/irc.freenode.net/#nairobilug'),
    ('Mailing List', 'https://groups.google.com/forum/#!forum/nairobi-gnu'),
)

# TODO: Not implemented
LINKS = (
    ('David Karibe', 'http://karibe.co.ke/'),
    ('Mjanja Tech', 'http://mjanja.co.ke/'),
    ('Moshe Njema', 'http://nj3ma.wordpress.com/'),
)

GITHUB_ADDRESS = 'https://github.com/nairobilug'
TWITTER_ADDRESS = 'https://twitter.com/nairobilug'
GPLUS_ADDRESS = 'https://plus.google.com/communities/107260210367217532462'

DISQUS_SITENAME = 'nairobilug'
GOOGLE_ANALYTICS_ID = 'UA-59440070-1'
