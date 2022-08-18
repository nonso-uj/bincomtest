from .base import *


SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [
    # change
    'bincom-poll-app.herokuapp.com',
]


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]


# DEBUG_PROPAGATE_EXCEPTIONS = True

# Heroku Logging

# LOGGING = {
#     'version': 1,
#     'dissable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineo)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging-StreamHandler',
#         },
#     },
#     'loggers': {
#         'MYAPP': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     }
# }






STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
