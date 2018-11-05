import os
from ddweb.settings.base import *  # noqa: F401, F403

DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = True  # noqa: F405
THUMBNAIL_DEBUG = True

SECRET_KEY = "This.is.not.a.secret.key"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "..", "ddweb.sqlite"),  # noqa: F405
    }
}
