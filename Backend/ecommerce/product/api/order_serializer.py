from ..models import Order
from rest_framework import serializers



class OrderListSerializer(serializers.ModelSerializer):
    # total_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id','user','total_price','is_paid','status','shipping_order']

    # def get_total_price(self,obj):
    #     return obj.update_total_price()
    
class OrderDetailSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id','total_price','is_paid','status','shipping_order']

    def get_total_price(self,obj):
        return obj.update_total_price()
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)