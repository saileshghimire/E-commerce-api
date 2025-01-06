from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .subcategory_serializer import SubCategorySerializer, SubCategoryViewSerializer
from ..models import Category

class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return SubCategoryViewSerializer(*args, **kwargs)
        return SubCategorySerializer(*args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save()
        # return Response({"message":"SubCategory added"},status=status.HTTP_201_CREATED)

    
class subcategoryDetailview(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = {IsAuthenticated}
    lookup_field = 'id'

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'Get':
            return SubCategoryViewSerializer(*args, **kwargs)
        return SubCategoryViewSerializer(*args, **kwargs)
    
