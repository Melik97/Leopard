from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductAPIView(viewsets.ViewSet):

    def list(self, request, pk=None):
        queryset = Product.objects.filter(category__slug=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        data = request.data
        product = Product.objects.create(
            name=data['name'],
            slug=data['slug'],
            image=data['image'],
            description=data['description'],
            price=data['price'],
            status=data['status'],
            category=Category.objects.get(slug=pk)
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        category = Product.objects.get(pk=pk)
        serializer = ProductSerializer(category)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # if data['name] is None you must use product data
    def update(self, request, pk=None):
        data = request.data
        product = Product.objects.get(pk=pk)
        product.name = data['name']
        product.slug = data['slug']
        product.image = data['image']
        product.description = data['description']
        product.price = data['price']
        product.status = data['status']

        serializer = ProductSerializer(product)
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

     # if data['name] is None you must use category data
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
