#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'TonyZhou'
SITENAME = u"H.B.Zhou's blog"
#SITEURL = 'http://tonyzhou.github.com'
SITEURL = 'http://tonyzhou.github.io'
TIMEZONE = 'Asia/Shanghai'
THEME = "/Users/Biu/Projects/SkyDrive/pelican-themes/fresh"

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_CATEGORIES_FROM_MENU = True
MENUITEMS = [('Blog', 'http://tonyzhou.github.io/index.html'),('Archives', 'http://tonyzhou.github.io/archives.html')]

GITHUB_URL = 'http://github.com/tonyzhou/'
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

DISQUS_SITENAME = "hbzhousblog"


# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('Diving for fun', 'http://9pm.me'))


# Social widget
SOCIAL = (('github', 'http://github.com/tonyzhou'),
        )

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
