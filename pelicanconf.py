from __future__ import unicode_literals


# Pelican settings ------------------------------------------------------------

# Basic
SITENAME = 'Nairobi LUG'
SITEURL = 'http://nairobilug.or.ke'

AUTHOR = 'Multiple'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
THEME = 'theme/alchemy'
TIMEZONE = 'Africa/Nairobi'

# Feeds
FEED_ATOM = 'feed/atom.xml'
FEED_RSS = 'feed/rss.xml'

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
}


# Theme settings --------------------------------------------------------------

PROFILE_IMAGE = '/images/profile.png'
SHOW_ARTICLE_AUTHOR = True
SITE_SUBTEXT = 'Nairobi GNU/Linux Users Group'

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

DISQUS_SITENAME = 'nairobilug'
GOOGLE_ANALYTICS_DOMAIN = 'nairobilug.or.ke'
GOOGLE_ANALYTICS_ID = 'UA-730843-9'
