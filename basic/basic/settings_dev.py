"""
開発環境用

Django settings for basic project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0=$=m-h6yw3cv=ppe@3&+_$#26m7^0%*+vcgn8za-5sq#qtvnt"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev",
        },
    },
    "formatters": {
        "dev": {
            "format": "\t".join(
                [
                    "%(asctime)s",
                    "[%(levelname)s]",
                    "%(pathname)s(Line:%(lineno)d)",
                    "%(message)s",
                ]
            ),
        }
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
