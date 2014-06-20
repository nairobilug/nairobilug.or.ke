#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Multiple'
SITENAME = 'Nairobi LUG'
SITEURL = 'http://nairobilug.or.ke'

DEFAULT_LANG = 'en'
TIMEZONE = 'Africa/Nairobi'

# Feed generation is usually not desired when developing
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None

# Top nav menu items
MENU_ITEMS = (
    ('Home','/'),
    ('Mailing list', 'https://groups.google.com/forum/#!forum/nairobi-gnu'),
)

# Blogroll
LINKS = (
    ('David Karibe', 'http://karibe.co.ke/'),
    ('Mjanja Tech', 'http://mjanja.co.ke/'),
    ('Moshe Njema', 'http://nj3ma.wordpress.com/'),
)

# Enable Disqus comments
DISQUS_SITENAME = "nairobilug"

# Enable Google Analytics
GOOGLE_ANALYTICS_ID = 'UA-730843-9'
GOOGLE_ANALYTICS_DOMAIN = 'nairobilug.or.ke'

# Alchemy theme settings
GITHUB_ADDRESS = 'https://github.com/nairobilug'
PROFILE_IMAGE = '/images/profile.png'
SITE_SUBTEXT = 'Nairobi GNU/Linux Users Group'
TWITTER_ADDRESS = 'https://twitter.com/nairobilug'

DEFAULT_PAGINATION = 10
THEME = 'pelican-alchemy/alchemy'
FEED_RSS = 'feed/rss.xml'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'

# Copy CNAME to output root
STATIC_PATHS = [
    'extra/CNAME',
    'images',
    ]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    }

# Clean output directory during build
DELETE_OUTPUT_DIRECTORY = True

# Show article author on posts
SHOW_ARTICLE_AUTHOR = True
