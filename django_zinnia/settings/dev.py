"""
Django settings for django_zinnia project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3vf8t+$@^&*i@915jk9oqmi2hum3k*#924v--tezp5q@bcwh$&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# -------------------------- 必须要加，否则访问不了首页 ------------------------------ #
# 必须要加，否则访问不了首页
SITE_ID = 1


# ------------------------------ 配置应用 ------------------------------ #
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # zinnia项目添加的app
    'django.contrib.sites',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia_bootstrap',
    'zinnia',

    # 自己添加的app
    #'users',
]


# ------------------------------ 配置中间件 ------------------------------ #
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ------------------------------ 配置根路由 ------------------------------ #
ROOT_URLCONF = 'django_zinnia.urls'


# ------------------------------ 配置模板 ------------------------------ #
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],

        # 使用bootstrap主题需要设置APP_DIRS=False，并添加'loaders'选项的一些设置
        'APP_DIRS': False,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            # 使用bootstrap主题需要添加如下几句
            'loaders': [
               'app_namespace.Loader',
               'django.template.loaders.filesystem.Loader',
               'django.template.loaders.app_directories.Loader',
            ],

        },
    },
]

# ------------------------------ 配置uwsgi ------------------------------ #
WSGI_APPLICATION = 'django_zinnia.wsgi.application'


# ------------------------------ 配置mysql数据库 ------------------------------ #
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql_pw_3',  # 数据库用户密码
        'NAME': 'django_zinnia'  # 数据库名字
    }
}


# ------------------------------ 密码验证 ------------------------------ #
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# ------------------------------ 配置时区/语言 ------------------------------ #
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ------------------------------ 设置静态文件目录 ------------------------------ #
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


# ------------------------------ 设置markdown ------------------------------ #
# 指明了使用 markdown 语法标记
ZINNIA_MARKUP_LANGUAGE = 'markdown'
# 指明markdown其它扩展以及语法高亮
ZINNIA_MARKDOWN_EXTENSIONS = ['markdown.extensions.extra', 'markdown.extensions.codehilite']

