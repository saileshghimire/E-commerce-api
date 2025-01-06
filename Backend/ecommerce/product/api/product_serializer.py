from ..models import Product, Category
from rest_framework import serializers

class CategoryForProductListSerilizer(serializers.ModelSerializer):
    parent_catgeory = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name']

    def get_parent_category(self, obj):
        if obj.parent_categeory is not None:
            return CategoryForProductListSerilizer(obj.parent_category).data
        return None

class ProductListSerilizer(serializers.ModelSerializer):
    category = CategoryForProductListSerilizer()

    class Meta:
        model = Product
        fields = ['id','name','category', 'price','get_discount_price','is_in_stock','description','sku','image']
        

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset= Category.objects.all())

    class Meta:
        model = Product
        fields = ['id','name','category', 'price','discount_price','description','stock_quantity','sku','image']
        extra_kwargs = {
            'image':{'required':False}
        }

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create( **validated_data)



class ProductListDetailSerializer(serializers.ModelSerializer):
    category = CategoryForProductListSerilizer()

    class Meta:
        model = Product
        fields = ['id','name','category', 'price','discount_price','description','stock_quantity','sku','image']