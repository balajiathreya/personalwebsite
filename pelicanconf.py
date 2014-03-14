#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Balaji Athreya'
SITENAME = u'Balaji Athreya'
SITEURL = 'balajiathreya.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/athreya86'),
          ('Linkedin', 'http://www.linkedin.com/in/balajiathreya/'),)

DEFAULT_PAGINATION = 10

THEME="../pelican-themes/gum"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
