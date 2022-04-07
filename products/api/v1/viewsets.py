from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Category, SubCategory, Post, PostImage
from products.api.v1.serializers import CategorySerializer, SubCategorySerializer, PostImageSerializer,\
    CarPostSerializer, LandAndPlotPostSerializer, GetPostSerializer
from django.db.models import Q, Count


def modify_input_for_multiple_files(post, image):
    dict = {}
    dict['post'] = post
    dict['image'] = image
    return dict


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["get"]


class SubCategoryViewSet(APIView):
    serializer_class = SubCategorySerializer

    def get(self, request, id=None):
        if id:
            sub_categories = SubCategory.objects.filter(category=id)
            serializer = self.serializer_class(sub_categories, many=True)
            return Response({"response": serializer.data}, status=status.HTTP_200_OK)
        sub_categories = SubCategory.objects.all()
        serializer = self.serializer_class(sub_categories, many=True)
        return Response({'response': serializer.data}, status=status.HTTP_200_OK)


class GetImageViewSet(APIView):
    serializer_class = PostImageSerializer

    def get(self, request, id=None):
        if id is not None:
            images = PostImage.objects.filter(id=id)
            serializer = self.serializer_class(images, many=True)
            return Response({"respone": serializer.data}, status=status.HTTP_200_OK)
        return Response({"response": "Given id is not exist"}, status=status.HTTP_400_BAD_REQUEST)


class PostImageViewSet(APIView):
    serializer_class = PostImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        post = request.data['post']

        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(post,
                                                            img_name)
            file_serializer = PostImageSerializer(data=modified_data)
            if file_serializer.is_valid(raise_exception=True):
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)


class GetDataBySubCategoryView(APIView):
    serializer_class = GetPostSerializer

    def get(self, request, sub_category):
        posts_by_sub_category = Post.objects.filter(sub_category__title__iexact=sub_category)
        serializer = self.serializer_class(posts_by_sub_category, many=True)
        return Response({"response": serializer.data}, status=status.HTTP_200_OK)


class GetAllPostAdsViewSet(ModelViewSet):
    serializer_class = GetPostSerializer
    queryset = Post.objects.all()
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category')
        sub_category = request.query_params.get('sub_category')
        location = request.query_params.get('location')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        posts = ""
        if category is None and sub_category is None and location is None and min_price is None and max_price is None:
            posts = self.queryset
        if category:
            posts = self.queryset.filter(category__title__iexact=category)
        if sub_category:
            posts = self.queryset.filter(sub_category__title__iexact=sub_category)
        if location:
            posts = self.queryset.filter(location__iexact=location)
        if min_price and max_price:
            posts = self.queryset.filter(price__lte=max_price, price__gte=min_price)

        serializer = self.get_serializer(posts, many=True)
        return Response({"response": serializer.data}, status=status.HTTP_200_OK)


class GetDataByUserView(APIView):
    serializer_class = GetPostSerializer

    def get(self, request, user_id):
        posts = Post.objects.filter(user_id=user_id)
        current_status = request.query_params.get('status')
        if current_status:
            posts = Post.objects.filter(user_id=user_id, status=current_status)
        serializer = self.serializer_class(posts, many=True)
        return Response({"response": serializer.data}, status=status.HTTP_200_OK)


class CarPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CarPostSerializer
    http_method_names = ['post', 'head', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"response": "There some error"}, status=status.HTTP_400_BAD_REQUEST)


class LanAndPlotPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = LandAndPlotPostSerializer
    http_method_names = ['post', 'head', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"response": "There some error"}, status=status.HTTP_400_BAD_REQUEST)


class VehicleFilterView(APIView):
    serializer_class = GetPostSerializer

    def get(self, request, sub_category_title=None):
        response = {}
        queryset = Post.objects.filter(sub_category__title__iexact=sub_category_title)
        location = request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location__icontains=location)
        min_year = request.query_params.get('min_year')
        if min_year is not None:
            queryset = queryset.filter(year__gte=min_year)
        max_year = request.query_params.get('max_year')
        if max_year is not None:
            queryset = queryset.filter(year__lte=max_year)
        min_driven = request.query_params.get('min_km_driven')
        if min_driven is not None:
            queryset = queryset.filter(km_driven__gte=min_driven)
        max_driven = request.query_params.get('max_km_driven')
        if max_driven is not None:
            queryset = queryset.filter(km_driven__lte=max_driven)
        min_price = request.query_params.get('min_price')
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        max_price = request.query_params.get('max_price')
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        fuel = request.query_params.get('fuel')
        if fuel is not None:
            fuel = fuel.split(',')
            queryset = queryset.filter(fuel__in=fuel)
        registration = request.query_params.get('registration')
        if registration is not None:
            registration = registration.split(',')
            queryset = queryset.filter(registered_in__in=registration)
        condition = request.query_params.get('condition')
        if condition is not None:
            condition = condition.split(',')
            posts = queryset.filter(condition__in=condition)
        make = request.query_params.get('make')
        if make is not None:
            make = make.split(',')
            queryset = queryset.filter(make__in=make)
        model = request.query_params.get('model')
        if model is not None:
            model = model.split(',')
            queryset = queryset.filter(model__in=model)
        if request.query_params == {}:
            queryset = queryset
        serializer = self.serializer_class(queryset, many=True)
        response['response'] = serializer.data
        filter_set = Post.objects.filter(sub_category__title__iexact=sub_category_title)
        post_per_location = filter_set.values("location").annotate(count=Count('location'))
        for i in range(len(post_per_location)):
            key = post_per_location[0].get('location')
            value = post_per_location[0].get('count')
            response[key] = value
        post_per_city = filter_set.values("city").annotate(count=Count('city'))
        for i in range(len(post_per_location)):
            key = post_per_city[0].get('location')
            value = post_per_city[0].get('count')
            response[key] = value
        return Response({'res': response}, status=status.HTTP_200_OK)


class PropertyForSaleFilterView(APIView):
    serializer_class = GetPostSerializer

    def get(self, request, sub_category_title=None):
        response = {}
        queryset = Post.objects.filter(sub_category__title__iexact=sub_category_title)
        location = request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location__icontains=location)
        min_price = request.query_params.get('min_price')
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        max_price = request.query_params.get('max_price')
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        min_area = request.query_params.get('min_area')
        if min_area is not None:
            queryset = queryset.filter(area__gte=min_area)
        max_area = request.query_params.get('max_area')
        if max_area is not None:
            queryset = queryset.filter(area__lte=max_area)
        property_type = request.query_params.get('property_type')
        if property_type is not None:
            property_type = property_type.split(',')
            queryset = queryset.filter(area__in=property_type)
        features = request.query_params.get('features')
        if features is not None:
            features = features.split(',')
            queryset = queryset.filter(features__in=features)
        area_unit = request.query_params.get('area_unit')
        if area_unit is not None:
            queryset = queryset.filter(aria_unit__iexact=area_unit)
        if request.query_params == {}:
            queryset = queryset
        serializer = self.serializer_class(queryset, many=True)
        response['response'] = serializer.data
        filter_set = Post.objects.filter(sub_category__title__iexact=sub_category_title)
        post_per_location = filter_set.values("location").annotate(count=Count('location'))
        for i in range(len(post_per_location)):
            key = post_per_location[0].get('location')
            value = post_per_location[0].get('count')
            response[key] = value
        post_per_city = filter_set.values("city").annotate(count=Count('city'))
        for i in range(len(post_per_location)):
            key = post_per_city[0].get('location')
            value = post_per_city[0].get('count')
            response[key] = value
        return Response({'res': response}, status=status.HTTP_200_OK)



