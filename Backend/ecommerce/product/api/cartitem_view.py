from ..models import CartItem
from .cartitem_serializer import CartItemDetailSerializer, CartItemListSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CartItemListAPIView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CartItemListSerializer
        return CartItemDetailSerializer
    

class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CartItemListSerializer
        return CartItemDetailSerializer