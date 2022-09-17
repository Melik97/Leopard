from rest_framework import serializers

from .models import Product, Category, get_avilable_category





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


    def create(self, validated_data):
        return super().create(validated_data)

    def get(self, validated_data):
        return super().get(validated_data)