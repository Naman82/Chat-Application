from django.urls import path
from chats import consumers

websocket_urlpatterns=[
    path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
]