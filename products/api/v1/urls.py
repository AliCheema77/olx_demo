from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api.v1.viewsets import CategoryViewSet, SubCategoryViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")


urlpatterns = [
    path("", include(router.urls)),
    path("sub_categories/", SubCategoryViewSet.as_view(), name="categories"),
    path("sub_categories/<int:id>/", SubCategoryViewSet.as_view(), name="categories_id")
]
