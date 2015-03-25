#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Orkun Gunay'
SITENAME = u'Anlatabildiklerim'
SITEURL = 'http://gunluk.orkungunay.com'

PATH = 'content'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

## Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 100

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/orkung/Git_Repolari/diger/pelican-themes/built-texts"
#THEME = "/home/orkung/Git_Repolari/diger/pelican-themes/mnmlist"
PLUGIN_PATHS = ['/home/orkung/pelican-plugin/disqus_static']
#PLUGINS = ['gravatar', 'tipue_search']
PLUGINS = [u"disqus_static"]
DISQUS_SITENAME = u'anlatabildiklerim'
DISQUS_SECRET_KEY = u'gEpV4X6QFbJrPisSAAt7aN1OWqCLntciqKsmtOMpCE78HtE4P40BXcRZKLGSWqXy'
DISQUS_PUBLIC_KEY = u'nWMqc5eElK99H1Ah1B0bSS1eOD7szDGrtnohNYRj9JqQh1LEx13da5vLc7JrFW2O'

