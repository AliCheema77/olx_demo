from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api.v1.viewsets import CategoryViewSet, SubCategoryViewSet, PostImageViewSet, CarPostViewSet,\
    GetImageViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("car_post", CarPostViewSet, basename="car_post")

urlpatterns = [
    path("", include(router.urls)),
    path("sub_categories/", SubCategoryViewSet.as_view(), name="categories"),
    path("sub_categories/<int:id>/", SubCategoryViewSet.as_view(), name="categories_id"),
    path("get_image/<int:id>/", GetImageViewSet.as_view(), name="get_image"),
    path("post_image/", PostImageViewSet.as_view(), name="post_image")
]
