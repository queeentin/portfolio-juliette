AUTHOR = "Quentin"
SITENAME = "Juliette Nier"
SITEURL = ""

PATH = "content"
STATIC_PATHS = ["projets"]

THEME = "themes/juliette"

TIMEZONE = "UTC"

DEFAULT_LANG = "fr"

# Put pages at the root of the website
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

PAGE_LANG_URL = "{lang}/{slug}/"
PAGE_LANG_SAVE_AS = "{lang}/{slug}/index.html"

# Don"t generate useless pages on authors, categories, etc.
DIRECT_TEMPLATES = []
AUTHOR_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
ARTICLE_SAVE_AS = ""
ARTICLE_LANG_SAVE_AS = ""
CATEGORY_SAVE_AS = ""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True