import os
from ddweb.settings.base import * # pylint: disable=wildcard-import,unused-wildcard-import

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True
THUMBNAIL_DEBUG = True

SECRET_KEY = 'This.is.not.a.secret.key'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'ddweb.sqlite'),
    }
}
