from rest_framework import serializers
from products.models import Category, SubCategory, PostImage, Post


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'image']


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'category']


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ['id', 'post', 'image']


class CarPostSerializer(serializers.Serializer):
    pass
