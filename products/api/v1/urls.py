from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api.v1.viewsets import CategoryViewSet, SubCategoryViewSet, PostImageViewSet, CarPostViewSet,\
    GetImageViewSet, LanAndPlotPostViewSet, GetDataBySubCategoryView, GetDataByUserView, GetAllPostAdsViewSet,\
    VehicleFilterView

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("car_post", CarPostViewSet, basename="car_post")
router.register("land_post", LanAndPlotPostViewSet, basename="land_post")
router.register("plot_post", LanAndPlotPostViewSet, basename="plot_post")
router.register("get_all_posts", GetAllPostAdsViewSet, basename="get_all_post")

urlpatterns = [
    path("", include(router.urls)),
    path("sub_categories/", SubCategoryViewSet.as_view(), name="categories"),
    path("sub_categories/<int:id>/", SubCategoryViewSet.as_view(), name="categories_id"),
    path("get_image/<int:id>/", GetImageViewSet.as_view(), name="get_image"),
    path("post_image/", PostImageViewSet.as_view(), name="post_image"),
    path("get_by_sub_category/<str:sub_category>/", GetDataBySubCategoryView.as_view(), name="get_by_sub_category"),
    path("get_by_user/<int:user_id>/", GetDataByUserView.as_view(), name="get_by_user"),
    path("vehicle_filter/<str:sub_category_title>/", VehicleFilterView.as_view(), name="car_filter"),
]
