import os

from django.core.wsgi import get_wsgi_application
APP_NAME = 'siteroot.conf'
os.environ['DJANGO_SETTINGS_MODULE'] = APP_NAME + '.settings'

application = get_wsgi_application()
