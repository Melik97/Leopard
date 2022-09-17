from rest_framework import viewsets

from .models import Cart, Shop, Wallet, User
from .serializers import RegisterSellerSerializer, ShopSerilizer, \
    RegisterSerializer


class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_seller=False).all()
    serializer_class = RegisterSerializer


class RegisterSellerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_seller=True).all()
    serializer_class = RegisterSellerSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerilizer
