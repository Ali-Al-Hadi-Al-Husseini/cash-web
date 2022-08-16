"""
Django settings for cash project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
# from pickle import FALSE, TRUE
import django_heroku
from pathlib import Path
import os
# from .custom_middleware import Remove_server
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# DEBUG = True
DEBUG = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# for a real production app i would use enviroment variables but since this is only a personal project i wont
SECRET_KEY = 'A$f242^#$svasd*as&^%$1V#!B^$X@523c52323c3C%@#2c3fsdfd'

# SECURITY WARNING: don't run with debug turned on in production!
# "cashweb.herokuapp.com","herokuapp.com",".herokuapp.com"
ALLOWED_HOSTS = ["cashweb.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'corsheaders',
    'crispy_forms',
    'crispy_bootstrap5'
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",   
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cash.custom_middleware.Remove_server'

]

ROOT_URLCONF = 'cash.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cash.wsgi.application'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    #     'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'yourdatabasename.db'),
    # }
    'default': {
        'HOST' : 'ec2-34-248-169-69.eu-west-1.compute.amazonaws.com',
        'NAME' : 'd8lm2t5962uvbp',
        'USER' : 'kqzkzmhdonxpvv',
        'PORT' :'5432',
        'ENGINE': 'django.db.backends.postgresql',
        'PASSWORD' :'e560688136bd7506c5ede193a7257fc08ce337d89c2384988545b0c11832b28a' ,
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# ADMINS = [["lilo",'moudy.vliax@gmail.com'],'alihadi.alhousseini@gmail.com']
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = str(BASE_DIR) + "\\main\\static\\qrcode/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'cash','static')
STATICFILES_DIRS = [
#    str(BASE_DIR)+ '\\main\\static',
# os.path.join(BASE_DIR,'/main/static'),
   os.path.join(BASE_DIR, 'main','static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'
CORS_ALLOWED_ORIGINS = []


CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True

#security 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT  = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD  = True
SECURE_HSTS_SECONDS = 60


django_heroku.settings(locals())    