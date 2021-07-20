
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = os.path.dirname(__file__).split(os.path.sep)[-2]
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, r'../../..'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=lr_c(&x_-x&i!zm7sicmg@j0t!6r4$d+l-5a8$_i+j72di0(%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework_api_key',
    'django_filters',
    'auth1',
    'project',
    'content',
    'survey',
    'django.contrib.admindocs'
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    # ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #         'rest_framework.permissions.IsAuthenticated',
    #     ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend', 'rest_framework.filters.OrderingFilter'],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework_api_key.permissions.HasAPIKey",
    ]

}

ROOT_URLCONF = '%s.urls' % APP_NAME

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

WSGI_APPLICATION = 'siteroot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3sngdjmtpu3t0',
        'USER': 'elgxciebplyenp',
        'PASSWORD': '2feb1f6a82213d48a6d9f20468c758233afd70a36cb3088bf3f00d724015b3bd',
        'HOST': 'ec2-52-6-77-239.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
#print(STATICFILES_DIRS)

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'wl@cmundp.de'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 465

try:
    from .local_settings import *
except ImportError:
    pass