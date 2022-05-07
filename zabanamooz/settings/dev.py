from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-=a)pnkp=6t&j2#fjj27s+-i(n872x*)hxbv5_ji+q0e!9jis_9'

ALLOWED_HOSTS = ['*']

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# These block are for testing gmail based mail service:

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'ebikdeli@gmail.com'
# EMAIL_HOST_PASSWORD = '<received password>'

# Remember: To be able to send email via other services like gmail or yahoo mail, we should activate ability to that:
# https://www.sitepoint.com/django-send-email/


try:
    from .local import *
except ImportError:
    pass
