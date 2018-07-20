from .base import *

secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json'), 'rb'))

DEBUG = False
ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

WSGI_APPLICATION = 'config.wsgi.production.application'

# DB
DATABASES = secrets['DATABASES']
print(DATABASES)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
