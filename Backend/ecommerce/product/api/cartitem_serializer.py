from ..models import CartItem, Product, Cart
from user_app.models import CustomUser
from rest_framework import serializers

class ProductForCartItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name']

class CartItemListSerializer(serializers.ModelField):
    product = ProductForCartItemListSerializer()
    class Meta:
        model = CartItem
        fields = ['id','product','quantity']

    


class CartItemDetailSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(quweryset=Product.objects.all())
    class Meta:
        model = CartItem
        fields = ['id','product','quantity']

    def create(self, validated_data):
        cart = Cart.objects.get_or_create(user=self.context['request'].user)
        validated_data['cart'] = cart
        return super().create(validated_data)

