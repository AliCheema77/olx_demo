from django.urls import path, include
from products import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:groupName>/', consumers.MySyncConsumerDynamicGroup.as_asgi()),
]
