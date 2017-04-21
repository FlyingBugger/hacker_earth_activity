from base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'hacker_earth_db',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':3306,
        'OPTIONS':{

        }
    }
}

DEV_PROJECT_APPS = [
]

DEV_PROJECT_MIDDLEWARE = [
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS + DEV_PROJECT_APPS
MIDDLEWARE = PREREQ_MIDDLEWARE + PROJECT_MIDDLEWARE

# static files

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# media files (user-generated files)
MEDIA_ROOT = '/Users/yexianyong/Desktop/assets_upload/'