from base import *

DEBUG = False


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'hacker_earth_db',
        'USER':'xianyong',
        'PASSWORD':'123456',
        'HOST':'',
        'PORT':3306,
        'OPTIONS':{

        }
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS
MIDDLEWARE = PREREQ_MIDDLEWARE + PROJECT_MIDDLEWARE

STATIC_ROOT = os.path.join(os.path.abspath(os.path.join(BASE_DIR,os.pardir,os.pardir)), "static/")

MEDIA_ROOT = '/root/hacker_earth_activity/upload_assets'
