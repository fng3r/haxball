"""
Django settings for haxball_site project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm_5m)8w^h+8avxko^()kmlr6fnp(r+m1^=(m!kldx$*47(-za6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#try:
#   HOSTNAME = socket.gethostname()
#except:
#    HOSTNAME = 'localhost'

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['185.7.145.91','cis-haxball.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    # text-editors testing
    #'markdownx',
    'ckeditor',
    'django_summernote',
    'froala_editor',
    'ckeditor_uploader',
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

ROOT_URLCONF = 'haxball_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'haxball_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

X_FRAME_OPTIONS = 'SAMEORIGIN'

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'hax_db',
                'USER': 'kikimor24',
                'PASSWORD': 'gibby4mopolnoye322',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

USE_I18N = True

USE_L10N = True

USE_TZ = True


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
    ACCOUNT_EMAIL_VERIFICATION = True
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
    ACCOUNT_EMAIL_VERIFICATION = True
    # ACCOUNT_USERNAME_MIN_LENGTH = 1

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'haxballcis@gmail.com'
EMAIL_HOST_PASSWORD = 'ciscis08062020'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

if DEBUG:
    STATIC_URL = '/static/'
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [STATIC_DIR]
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = '/root/site/media'

CKEDITOR_UPLOAD_PATH = "uploads/"

LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

SITE_ID = 1

SUMMERNOTE_THEME = 'bs3'

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        'width': '100%',
        'height': '200',
        'js': {
        },
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'monokai',
        },
        'toolbar': [
            #['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['insert', ['link', 'picture', 'video']],
            # ['fontname', ['fontname']],
        ],

    },
    'js': (
        '/static/summernote-ext-print.js',
    ),
    'js_for_inplace': (
        '/static/summernote-ext-print.js',
    ),
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.40.0/theme/base16-dark.min.css',
    ),
    'css_for_inplace': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.40.0/theme/base16-dark.min.css',
    ),
    'codemirror': {
        'theme': 'base16-dark',
        'mode': 'htmlmixed',
        'lineNumbers': 'true',
    },
    'lazy': False,


}

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'height': 400,
        'width': '100%',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
                'Youtube'
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'youtube'
        ]),
    },
    'comment': {
        'skin': 'minimalist',
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'height': 100,
        'width': '200%',
        'toolbar':
            [
                ['Bold', 'Italic', 'Underline']
            ],
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'youtube'
        ])
    }
}
