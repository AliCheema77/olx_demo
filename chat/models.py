from django.db import models
from django.contrib.auth import get_user_model
from products.models import Post

User = get_user_model()


class Chat(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='chat_post')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_user')
    seller_message = models.CharField(max_length=1000, null=True, blank=True)
    seller_image = models.ImageField(upload_to='chat/', null=True, blank=True)
    buyer_message = models.CharField(max_length=1000, null=True, blank=True)
    buyer_image = models.ImageField(upload_to='chat/', null=True, blank=True)

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.ad_title
