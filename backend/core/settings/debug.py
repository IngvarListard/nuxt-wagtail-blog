from .production import *
from corsheaders.defaults import default_headers

ALLOWED_HOSTS.extend(('localhost', '127.0.0.1'))

# cors-headers for developer server
INSTALLED_APPS.append('corsheaders')
CORS_ORIGIN_WHITELIST = ('http://localhost:3000', 'http://127.0.0.1:3000')
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = default_headers + ('cache-control',)
CSRF_TRUSTED_ORIGINS = ['localhost:8080', '127.0.0.1:8080', 'localhost']
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')


# Батчинг graphql запросов
GRAPHQL_BATCH = False

DJANGOENV = 'development'

# Logging
if ENABLE_DB_LOG:
    LOGGING['handlers']['db_file'] = {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': './db.log',
    }
    LOGGING['loggers']['django.db.backends'] = {
        'handlers': ['db_file'],
        'level': 'DEBUG',
        'propagate': True,
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

