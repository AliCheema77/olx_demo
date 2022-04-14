from django.contrib import admin
from products.models import Category, SubCategory, PostImage, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['ad_title', 'description', 'created', 'updated']
