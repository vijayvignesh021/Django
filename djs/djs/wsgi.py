<<<<<<< HEAD
"""
WSGI config for djs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djs.settings')

application = get_wsgi_application()
=======
"""
WSGI config for djs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djs.settings')

application = get_wsgi_application()
>>>>>>> 58c2781f6e12362f31ad786b6796c2773cf0ab3e
