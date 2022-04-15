from django.db import models
from django.contrib.auth import get_user_model
from products.models import Post

User = get_user_model()


class Chat(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='chat_post')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_user')
    message = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='chat/', null=True, blank=True)

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.ad_title


class ChatGroup(models.Model):
    username = models.CharField(max_length=100)
    seller_image = models.ImageField(upload_to='chat/', null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_chat_group", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_chat_group", null=True, blank=True)
    post_title = models.CharField(max_length=250)
    last_message = models.CharField(max_length=1000)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_group')

    def __str__(self):
        return self.username
