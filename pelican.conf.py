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

# Blogroll
LINKS = (
    ('David Karibe', 'http://karibe.co.ke/'),
    ('Mjanja Tech', 'http://mjanja.co.ke/'),
    ('Moshe Njema', 'http://nj3ma.wordpress.com/'),
)

# Social widget
SOCIAL = (
    ('Nairobi GNU/Linux mailing list', 'https://groups.google.com/forum/#!forum/nairobi-gnu'),
)

# Crowsfoot settings
GITHUB_ADDRESS = 'https://github.com/nairobilug'
PROFILE_IMAGE_URL = '/images/profile.png'
SITESUBTITLE = 'Nairobi GNU/Linux Users Group'
TWITTER_ADDRESS = 'https://twitter.com/nairobilug'

DEFAULT_PAGINATION = 10
THEME = 'crowsfoot'
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
    ]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    }
