from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import Cart, Shop, User, Wallet


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'phone_number')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        user = User.objects.create(
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            password=make_password(validated_data['password']),
            email=validated_data['email'])

        return user


class RegisterSellerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'phone_number')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        seller = User.objects.create(
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            password=make_password(validated_data['password']),
            email=validated_data['email'],
            is_seller=True)

        return seller


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1


class WalletSerilizer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
        depth = 1


class ShopSerilizer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        depth = 1
