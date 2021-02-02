"""
Django Project Settings | Cannlytics API
Created: 2/1/2021

Django settings powered by environment variables and
secured by Google Cloud Secret Manager.
"""
import environ
import os

#------------------------------------------------------------#
# Project variables.
#------------------------------------------------------------#
PROJECT_NAME = "cannlytics_api"
ROOT_URLCONF = "cannlytics_api.urls"
SETTINGS_NAME = "cannlytics_api_settings"
WSGI_APPLICATION = "cannlytics_api.wsgi.application"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#------------------------------------------------------------#
# Environment variables
# https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key
#------------------------------------------------------------#
env_file = os.path.join(BASE_DIR, ".env")
if not os.path.isfile(".env"):
    import google.auth
    from google.cloud import secretmanager as sm
    _, project = google.auth.default()
    if project:
        client = sm.SecretManagerServiceClient()
        path = client.secret_version_path(project, SETTINGS_NAME, "latest")
        payload = client.access_secret_version(path).payload.data.decode("UTF-8")
        with open(env_file, "w") as f:
            f.write(payload)
env = environ.Env()
env.read_env(env_file)
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

#------------------------------------------------------------#
# Apps
# https://docs.djangoproject.com/en/3.1/ref/applications/
#------------------------------------------------------------#
INSTALLED_APPS = [
    "cannlytics_api",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "rest_framework",
]

#------------------------------------------------------------#
# Middleware
# https://docs.djangoproject.com/en/3.1/topics/http/middleware/
#------------------------------------------------------------#
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#------------------------------------------------------------#
# Templates
# https://docs.djangoproject.com/en/3.1/ref/templates/language/
#------------------------------------------------------------#
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

#------------------------------------------------------------#
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
#------------------------------------------------------------#
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Los_Angeles"
USE_I18N = True
USE_L10N = True
USE_TZ = True

#------------------------------------------------------------#
# Security
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/web_application_security
#------------------------------------------------------------#
ALLOWED_HOSTS = [
    "*",  # TODO: DANGEROUS! Remove in production.
    "localhost:8000",
    "127.0.0.1",
    "api.cannlytics.com",
    "cannlytics-api.web.app",
]

SECURE_SSL_REDIRECT = False

#------------------------------------------------------------#
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#------------------------------------------------------------#
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
