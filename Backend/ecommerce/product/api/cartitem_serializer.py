from ..models import CartItem, Product
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
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

