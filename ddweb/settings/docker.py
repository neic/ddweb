from ddweb.settings.base import * # pylint: disable=wildcard-import,unused-wildcard-import

DEBUG = True
TEMPLATE_DEBUG = False

ADMINS = (
    ('Mathias Dannesbo', 'webmaster@danishdecoration.dk'),
)
MANAGERS = ADMINS

# Generate using pwgen -sy 50 1
SECRET_KEY = '...'

ALLOWED_HOSTS = ['danishdecoration.dk',
                 'www.danishdecoration.dk']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "postgres",
        'USER': "postgres",
        'HOST': "db",
        'PORT': 5432,
    }
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ddweb.wsgi.application'


MEDIA_ROOT = '/media'
STATIC_ROOT = '/static'
