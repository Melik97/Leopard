import email
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Cart, Shop, Wallet, User
from .serializers import RegisterSellerSerializer, ShopSerilizer, \
    RegisterSerializer


class RegisterUserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.filter(is_seller=False).all()
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = RegisterSerializer(data)
        return Response(serializer.data)


class RegisterSellerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.filter(is_seller=True).all()
        serializer = RegisterSellerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = RegisterSellerSerializer(data)
        return Response(serializer.data)


class ShopViewSet(viewsets.ViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerilizer
