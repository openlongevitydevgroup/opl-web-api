from os import environ
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables
load_dotenv("./OPL/config.env")

match (environ.get("WEB_API_URLS")):
    case str(value):
        web_api_urls = value.split("|")
    case _:
        web_api_urls = []

match (environ.get("SPA_URLS")):
    case str(value):
        spa_urls = value.split("|")
    case _:
        spa_urls = []

match (environ.get("DEBUG_MODE")):
    case str(value):
        debug_mode = value.lower() == "true"
    case _:
        debug_mode = []

cwd_path = Path.cwd()

SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = debug_mode
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "open_problems",
    "posts_comments",
    "annotations",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
ROOT_URLCONF = "OPL.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(cwd_path.joinpath("templates")),
            str(cwd_path.joinpath("questions", "templates")),
        ],
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
WSGI_APPLICATION = "OPL.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ.get("DB_NAME"),
        "USER": environ.get("DB_USER"),
        "PASSWORD": environ.get("DB_PASSWORD"),
        "HOST": environ.get("DB_HOST"),
        "PORT": environ.get("DB_PORT"),
    }
}
STATIC_URL = "static/"
STATIC_ROOT = str(cwd_path.joinpath("staticfiles"))
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
