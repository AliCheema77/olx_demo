from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_post")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="sub_category_post")
    ad_title = models.CharField(max_length=70)
    description = models.TextField(max_length=4096)
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900)], null=True, blank=True)
    km_driven = models.PositiveIntegerField(null=True, blank=True)
    fuel = models.CharField(max_length=100, null=True, blank=True)
    registered_in = models.CharField(max_length=100, null=True, blank=True)
    condition = models.CharField(choices=(('new', 'New'), ('used', 'Used')), max_length=10, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    # features = models.CharField(max_length=100, null=True, blank=True)
    features = ArrayField(
            models.CharField(max_length=250, blank=True, null=True),
            size=50,
            null=True, blank=True
    )
    aria_unit = models.CharField(choices=(('kanal', 'Kanal'), ('marla', 'Marla'), ('square_feet', 'Square Feet'),
                                          ('square_meter', 'Square Meter'), ('square_yards', 'Square Yards')),
                                 null=True, blank=True, max_length=30)
    area = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    show_phone_number = models.BooleanField(default=False)

    def __str__(self):
        return self.ad_title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.post.ad_title

    class Meta:
        verbose_name = "Post Image"
        verbose_name_plural = "Post Images"

