from .order_serializer import OrderListSerializer, OrderDetailSerializer
from ..models import Order
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderListSerializer
        return OrderDetailSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderDetailSerializer
    lookup_field = 'id'