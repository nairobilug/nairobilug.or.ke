#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Multiple'
SITENAME = 'Nairobi GNU/Linux Users Group'
SITEURL = 'http://nairobilug.or.ke'

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
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

DEFAULT_PAGINATION = 10

THEME = 'crowsfoot'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'

# Copy CNAME to output root
FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
)

GITHUB_URL = 'http://github.com/nairobilug/'
