from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductAPIView, CategoryAPIView


router = DefaultRouter()
router.register(
    r'categories',
    CategoryAPIView,
    basename="categories"
    )
router.register(
    r'categories/<str:pk>',
    CategoryAPIView,
    basename="category"
    )


router2 = DefaultRouter()
router2.register(
    r'products',
    ProductAPIView,
    basename="category-products-list"
    )
router2.register(
    r'products/<int:pk2>',
    ProductAPIView,
    basename="category-product"
    )


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('category/<str:pk>/', include(router2.urls)),
]
