from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from .views import RegisterUserViewSet, RegisterSellerViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(
    r'register/users',
    RegisterUserViewSet,
    basename="register-users"
    )
router.register(
    r'register/sellers',
    RegisterSellerViewSet,
    basename="register-sellers"
    )
router.register(
    r'register/seller/<int:pk>/shops',
    RegisterSellerViewSet,
    basename="seller-shops"
    )


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
