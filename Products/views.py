from django.shortcuts import get_object_or_404
from matplotlib.pyplot import get
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = ProductSerializer(data)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=pk)
        category.delete()
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data
        queryset = Category.objects.all()

        category = get_object_or_404(queryset, slug=pk)
        category.name = data['name']
        category.slug = data['slug']
        category.is_sub = data['is_sub']
        if data['is_sub'] == 'False':
            category.save_base = Category.objects.get(
                    slug=data['sub_category_slug'])

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        category = get_object_or_404(queryset, slug=pk)
        serializer = ProductSerializer(category)
        return Response(serializer.data)


class CategoryAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        if data['is_sub'] == 'False':
            category = Category.objects.create(
                name=data['name'],
                slug=data['slug'],
                is_sub=data['is_sub'],
                sub_category=Category.objects.get(
                    slug=data['sub_category_slug'])
            )

        else:
            category = Category.objects.create(
                name=data['name'],
                slug=data['slug'],
                is_sub=data['is_sub'],
            )

        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=category)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=pk)
        category.delete()
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data
        queryset = Category.objects.all()

        category = get_object_or_404(queryset, slug=pk)
        category.name = data['name']
        category.slug = data['slug']
        category.is_sub = data['is_sub']
        if data['is_sub'] == 'False':
            category.save_base = Category.objects.get(
                    slug=data['sub_category_slug'])

        serializer = CategorySerializer(category)
        return Response(serializer.data)
