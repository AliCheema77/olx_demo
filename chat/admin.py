from django.contrib import admin
from chat.models import Chat, ChatGroup


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['post', 'buyer', 'message', 'image']


@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ['username', 'post_title', 'last_message', 'buyer', 'seller', 'seller_image', 'post']
