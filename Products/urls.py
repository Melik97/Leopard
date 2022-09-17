from django.urls import path

from .views import ProductAPIView, CategoryAPIView


urlpatterns = [
    path(
        'categories/products',
        ProductAPIView.as_view(),
        name='home'
    ),
    path(
        'categories/',
        CategoryAPIView.as_view(),
        name='categories'
    ),
    path(
        'categories/<str:slug>/',
        CategoryAPIView.as_view(),
        name='categorie'
    ),
]
