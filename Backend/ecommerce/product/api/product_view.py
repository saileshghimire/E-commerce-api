from rest_framework_simplejwt.authentication import JWTAuthentication
from .product_serializer import ProductListSerilizer, ProductDetailSerializer,ProductListDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from ..models import Product

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerilizer
        return ProductDetailSerializer

    # def get_serializer(self, *args, **kwargs):
    #     if self.request.method == 'GET':
    #         return ProductListSerilizer(*args, **kwargs)
    #     return ProductDetailSerializer(*args, **kwargs)
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return ProductListDetailSerializer(*args, **kwargs)
        return ProductDetailSerializer(*args, **kwargs)