from .common import *

PUBLIC_REGISTER_ENABLED = True
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '$TAIGA_SECRET'

MEDIA_URL = "$TAIGA_SCHEME://$TAIGA_HOST$TAIGA_PORT/media/"
STATIC_URL = "$TAIGA_SCHEME://$TAIGA_HOST$TAIGA_PORT/static/"
ADMIN_MEDIA_PREFIX = "$TAIGA_SCHEME://$TAIGA_HOST$TAIGA_PORT/static/admin/"
SITES["api"]["scheme"] = "$TAIGA_SCHEME"
SITES["api"]["domain"] = "$TAIGA_HOST"
SITES["front"]["scheme"] = "$TAIGA_SCHEME"
SITES["front"]["domain"] = "$TAIGA_HOST"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "$POSTGRES_DB",
        "HOST": "$POSTGRES_HOST",
        "USER": "$POSTGRES_USER",
        "PASSWORD": "$POSTGRES_PASSWORD"
    }
}

#DEFAULT_FROM_EMAIL = "john@doe.com"
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False # You cannot use both (TLS and SSL) at the same time!
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://$RABBIT_USER:$RABBIT_PASSWORD@$RABBIT_HOST:$RABBIT_PORT/$RABBIT_VHOST"}

CELERY_ENABLED = True

# GitLab
INSTALLED_APPS += ["taiga_contrib_gitlab_auth"]

# Get these from Admin -> Applications
GITLAB_API_CLIENT_ID = "$GITLAB_API_CLIENT_ID"
GITLAB_API_CLIENT_SECRET = "$GITLAB_API_CLIENT_SECRET"
GITLAB_URL = "$GITLAB_URL"
