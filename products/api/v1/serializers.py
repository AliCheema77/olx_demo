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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        data['post'] = instance.post.user.username
        return data


class CarPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'user', 'category', 'sub_category', 'ad_title', 'description', 'make', 'model', 'year',
                  'km_driven', 'fuel', 'registered_in', 'condition', 'price', 'location', 'city', 'phone_number',
                  'show_phone_number']
