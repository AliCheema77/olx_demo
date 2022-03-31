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


class GetDataBySubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class GetDataByUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class CarPostSerializer(serializers.ModelSerializer):
    image = PostImageSerializer(source='post', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'category', 'sub_category', 'ad_title', 'description', 'make', 'model', 'year',
                  'km_driven', 'fuel', 'registered_in', 'condition', 'image', 'price', 'location',
                  'city', 'name', 'phone_number', 'show_phone_number']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        data['category'] = instance.category.title
        data['sub_category'] = instance.sub_category.title
        return data


class LandAndPlotPostSerializer(serializers.ModelSerializer):
    image = PostImageSerializer(source='post', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'category', 'sub_category', 'ad_title', 'description', 'type', 'features', 'aria_unit',
                  'area', 'image', 'price', 'location', 'city', 'name', 'phone_number',
                  'show_phone_number']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        data['category'] = instance.category.title
        data['sub_category'] = instance.sub_category.title
        return data
