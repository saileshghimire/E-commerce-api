from ..models import Cart, CartItem
from rest_framework import serializers
from .cartitem_serializer import CartItemListSerializer

class CartListSerializer(serializers.ModelSerializer):
    cart_items = CartItemListSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','cart_items','total_price','user']

    def get_toal_price(self,obj):
        return obj.get_total_price()
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    