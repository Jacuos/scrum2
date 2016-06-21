"""
WSGI config for scrum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from asgiref.wsgi import WsgiToAsgiAdapter
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrum.settings")

channel_layer = get_channel_layer()
application = WsgiToAsgiAdapter(channel_layer)
