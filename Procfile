web: gunicorn tutorial.wsgi

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "findtheirgifts.settings")

application = get_wsgi_application()