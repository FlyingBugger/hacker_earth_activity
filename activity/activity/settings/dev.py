from base import *




DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'hacker_earth_db',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'',
        'PORT':3306,
        'OPTIONS':{

        }
    }
}


