from base import *

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Mathias Dannesbo', 'webmaster@danishdecoration.dk'),
)
MANAGERS = ADMINS

# Generate using pwgen -sy 50 1
SECRET_KEY = '...'

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {}
