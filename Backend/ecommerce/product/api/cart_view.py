from ..models import Cart
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .cart_serializer import CartListSerializer

class CartListAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartListSerializer
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)