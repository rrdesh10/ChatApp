"""
ASGI config for chatsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLResolver
import chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatsite.settings')

application = ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket':AuthMiddlewareStack(
            URLResolver(
                pattern= chatapp.routing.websocket_urlpatterns,
                urlconf_name= ('chatapp.routing')
            )
        )
    }
)
