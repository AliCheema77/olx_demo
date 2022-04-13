from django.contrib import admin
from products.models import Category, SubCategory, PostImage, Post, Group, Chat


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


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'timestamp', 'group']