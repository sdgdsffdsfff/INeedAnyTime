"""
Django settings for AnyTime project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8$tvoil$@7o$omuxcvyaxq^#2k^_@awho_pvjfw)!)8qwqes48'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#TEMPLATE_DIR
TEMPLATE_DIRS=os.path.join(BASE_DIR,"templates").replace("\\","/")

ALLOWED_HOSTS = []

AUTHENTICATION_BACKENDS= (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas.backends.CASBackend',
)

#CAS INFO TestEnv URL
CAS_SERVER_URL="http://cas.uat.qa.nt.ctripcorp.com/caso/"
CAS_LOGOUT_COMPLETELY=True
CAS_IGNORE_REFERER=True
CAS_REDIRECT_URL="/"
CAS_AUTO_CREATE_USERS=True
CAS_GATEWAY=False
CAS_RETRY_LOGIN=True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AnyTimeHome',
    'django_cas'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_cas.middleware.CASMiddleware',
)

ROOT_URLCONF = 'AnyTime.urls'

WSGI_APPLICATION = 'AnyTime.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'natdb',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306'
    },
    'reportplatform':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'reportplatform',
        'USER':'root',
        'PASSWORD':'sonar',
        'HOST':'192.168.81.146',
        'PORT':'55666'
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
    ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ),
    ('upload',os.path.join(STATIC_ROOT,'upload').replace('\\','/') ),
)