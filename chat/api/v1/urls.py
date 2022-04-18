from django.urls import path
from chat.api.v1.viewsets import ChatView, ChatGroupView

urlpatterns = [
    path('chat/<int:post_id>/<int:buyer_id>/', ChatView.as_view(), name='chat'),
    path('delete_chat/<int:post_id>/<int:buyer_id>/', ChatView.as_view(), name='delete_chat'),
    path('chat_group/<int:user_id>/', ChatGroupView.as_view(), name='chat_group')
]
