from base import *

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'This.is.not.a.secret.key'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'ddweb.sqlite'),
    }
}


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ddweb.wsgi.application'
