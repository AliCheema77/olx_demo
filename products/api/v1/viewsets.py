from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Category, SubCategory, Post, PostImage
from products.api.v1.serializers import CategorySerializer, SubCategorySerializer, PostImageSerializer,\
    CarPostSerializer, LandAndPlotPostSerializer


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


class CarPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CarPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"response": "There some error"}, status=status.HTTP_400_BAD_REQUEST)


class LanAndPlotPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = LandAndPlotPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"response": "There some error"}, status=status.HTTP_400_BAD_REQUEST)


