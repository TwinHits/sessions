from .base import *

DEBUG = True

SECRET_KEY = get_env_variable("SECRET_KEY")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "sessions",
        "USER": "admin",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

STATICFILES_DIRS = (BASE_DIR.child("static"),)
STATIC_URL = '/static/'
