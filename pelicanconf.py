AUTHOR = 'Michael Ring'
SITENAME = 'Sufficiently Large Telescope Observatory'
SITESUBTITLE = 'Home of the SLT Team'
DESCRIPTION = 'A website about space, exploration and nice pictures...'
SITEURL = "https://slt-observatory.space"
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

META_IMAGE = SITEURL + "/static/img/slt_logo.jpg"
META_IMAGE_TYPE = "image/jpeg"

PATH = "content"
TIMEZONE = 'Europe/Zurich'
DEFAULT_LANG = 'de'
LOCALE = 'de_DE'
#THEME = "themes/mg-mir"
THEME = "themes/Flex"
#THEME = "themes/pelican-twitchy"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# This is just a hack to have the css uploaded automagically
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['pelican_javascript']

CUSTOM_CSS = "css/overridestyles.css"

# Blogroll
#LINKS = (
#    ("Pelican", "https://getpelican.com/"),
#)

DEFAULT_PAGINATION = False

PAGE_ORDER_BY = 'sortorder'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
#DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search')

#RELATIVE_URLS = False
RELATIVE_URLS = True

PAGES = (
  {'title': 'Home', 'url': 'pages/worum-geht-es.html'},
  {'title': 'Team', 'url': 'pages/team.html'},
  {'title': 'Impressum', 'url': 'pages/impressum.html'},
)

