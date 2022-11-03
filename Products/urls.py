from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductAPIView, CategoryAPIView


router = DefaultRouter()
router.register(
    r'categories/products',
    ProductAPIView,
    basename="products"
    )
router.register(
    r'categories/products/<str:pk>',
    ProductAPIView,
    basename="product"
    )

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


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
