from django.urls import path
from chat.api.v1.viewsets import ChatView

urlpatterns = [
    path('chat/<int:post_id>/<int:buyer_id>/', ChatView.as_view(), name='chat')
]