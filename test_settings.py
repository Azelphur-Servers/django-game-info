SECRET_KEY = "lorem ipsum"

INSTALLED_APPS = (
    'game_info',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'game_info.urls'
