from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='profile/', null=True, blank=True)
    image = models.CharField(max_length=250, null=True, blank=True)
    google_id = models.CharField(max_length=250, null=True, blank=True)


