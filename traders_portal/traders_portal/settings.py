import os
import environ

from pathlib import Path

from firebase_admin import credentials, initialize_app


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load env variables
env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--()&_yik3pmx7t%mo_75u^g&p3#e3+4f=_wun%f_@z!t^7g+71'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom Apps
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

ROOT_URLCONF = 'traders_portal.urls'

AUTH_USER_MODEL = 'users.Users'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'traders_portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Firebase 

FIREBASE_CONFIG_API_KEY = os.getenv('FIREBASE_CONFIG_API_KEY')
FIREBASE_CONFIG_AUTH_DOMAIN = os.getenv('FIREBASE_CONFIG_AUTH_DOMAIN')
FIREBASE_CONFIG_PROJECT_ID = os.getenv('FIREBASE_CONFIG_PROJECT_ID')
FIREBASE_CONFIG_STORAGEBUCKET = os.getenv('FIREBASE_CONFIG_STORAGEBUCKET')
FIREBASE_CONFIG_MESSAGING_SENDER_ID = os.getenv('FIREBASE_CONFIG_MESSAGING_SENDER_ID')
FIREBASE_CONFIG_APP_ID = os.getenv('FIREBASE_CONFIG_APP_ID')

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": os.getenv('FIREBASE_PROJECT_ID'),
  "private_key_id": os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
  "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace(r'\n', '\n'),
  "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
  "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ.get('FIREBASE_CLIENT_CERT_URL'),
  "universe_domain": "googleapis.com"
})

default_app = initialize_app(cred)

