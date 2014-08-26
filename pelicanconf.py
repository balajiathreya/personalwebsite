#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Balaji Athreya'
SITENAME = u'Balaji Athreya'
SITEURL = 'balajiathreya.com'
PATH = '/home/balaji/personalwebsite/content'
TWITTER_USERNAME = 'athreya86'
SITESUBTITLE = 'Yet another blog'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Resume', 'https://docs.google.com/document/d/14PTi6HTlyhq-_eKqlyozZWhLmQilcbJK99KmNX9TdiA/edit?usp=sharing'),('What am I reading right now?', 'https://www.goodreads.com/balajiathreya'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/athreya86'),
          ('Linkedin', 'http://www.linkedin.com/in/balajiathreya/'),
	  ('Github', 'https://github.com/balajiathreya'))


#DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_TAGS_ON_SIDEBAR = False


DEFAULT_PAGINATION = 10

THEME="../pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME='yeti'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


GOOGLE_ANALYTICS = "UA-26987021-2"
#GITHUB_USER="balajiathreya"
