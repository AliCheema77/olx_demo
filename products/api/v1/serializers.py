from rest_framework import serializers
from products.models import Category, SubCategory, PostImage, Post, Chat, Group


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'category']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class CategorySerializer(serializers.ModelSerializer):
    category = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'category']


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ['id', 'post', 'image']


class GetPostSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        data['category'] = instance.category.title
        data['sub_category'] = instance.sub_category.title
        return data


class CarPostSerializer(serializers.ModelSerializer):
    image = PostImageSerializer(source='post', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'category', 'sub_category', 'ad_title', 'description', 'make', 'model', 'year',
                  'km_driven', 'fuel', 'registered_in', 'condition', 'image', 'price', 'location',
                  'city', 'name', 'status', 'phone_number', 'show_phone_number', 'created', 'updated']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        data['category'] = instance.category.title
        data['sub_category'] = instance.sub_category.title
        return data


class LandAndPlotPostSerializer(serializers.ModelSerializer):
    image = PostImageSerializer(source='post', many=True, read_only=True)
    features = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Post
        fields = ['id', 'user', 'category', 'sub_category', 'ad_title', 'description', 'type', 'features', 'aria_unit',
                  'area', 'image', 'price', 'location', 'city', 'name', 'status', 'phone_number',
                  'show_phone_number', 'created', 'updated']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        data['category'] = instance.category.title
        data['sub_category'] = instance.sub_category.title
        return data


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
