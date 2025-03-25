import dj_database_url
from decouple import config
import os
from pathlib import Path

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')  # Get secret key from .env file
ALLOWED_HOSTS = ['simple-expense-84d01d0e9ff8.herokuapp.com', 'localhost', '127.0.0.1']


DEBUG = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'expenses',
    'whitenoise.runserver_nostatic',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
]

ROOT_URLCONF = 'simple_expense.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'simple_expense.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'), conn_max_age=600)
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

# For local development (static files served by Django itself)
STATICFILES_DIRS = [
    BASE_DIR / 'expenses' / 'static',
]

# For production (Whitenoise handling static files)
STATIC_ROOT = BASE_DIR / 'staticfiles' 

# Static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production 
SECURE_SSL_REDIRECT = False  # False for development
CSRF_COOKIE_SECURE = False   # False for development
SESSION_COOKIE_SECURE = False  # False for development
SECURE_CONTENT_TYPE_NOSNIFF = True
