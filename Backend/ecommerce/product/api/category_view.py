from rest_framework.response import Response
from rest_framework import generics
from ..models import Category
from product.api.category_serializer import CategoryListSerializer, CategotyDetailSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes =[IsAuthenticated]
    
    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return CategoryListSerializer(*args, **kwargs)
        return CategotyDetailSerializer(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return CategoryListSerializer(*args, **kwargs)
        return CategotyDetailSerializer(*args, **kwargs)
