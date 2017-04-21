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

MEDIA_ROOT = '/root/hacker_earth_activity/upload_assets'
