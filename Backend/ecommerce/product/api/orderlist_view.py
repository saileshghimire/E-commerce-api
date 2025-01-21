from ..models import OrderItem
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .orderlist_serializer import OrderItemSerializer,OrderItemDetailSerializer

class OrderItemListView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemDetailSerializer

class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemDetailSerializer
    