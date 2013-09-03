#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = u'TonyZhou'
SITENAME = u"H.B.Zhou's blog"
#SITEURL = 'http://tonyzhou.github.com'
SITEURL = 'http://localhost:8000'
TIMEZONE = 'Asia/Shanghai'

GITHUB_URL = 'http://github.com/tonyzhou/'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_DATE = (2013, 7, 21, 14, 1, 1)
DEFAULT_LANG = u'en'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('Diving for fun', 'http://9pm.me'))


# Social widget
SOCIAL = (('github', 'http://github.com/tonyzhou'),
        )

DEFAULT_PAGINATION = 15

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
