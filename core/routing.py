from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import anonymous.routing
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(
        anonymous.routing.websocket_urlpatterns
    )),
})