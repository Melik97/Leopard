from rest_framework import mixins, generics

from .models import Product, Category
from .serializers import ProductSerializer


class ProductAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, 
                        mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# class CategoryAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, 
#                         mixins.DestroyModelMixin, generics.GenericAPIView):

#     queryset = Category.objects.all()
#     serializer_class = MyModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

