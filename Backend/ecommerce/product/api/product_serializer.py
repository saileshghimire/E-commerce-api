from ..models import Product, Category
from rest_framework import serializers

class CategoryForProductListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SubCategoryForProductListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductListSerilizer(serializers.ModelSerializer):
    class Meta:
        category = serializers.PrimaryKeyRelatedField(queryset= Category.objects.all())
        subcategory = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
        model = Product
        fields = ['id','category','subcategory', 'price','discount_price','description','stock_quantity','sku','image']
        extra_kwargs = {
            'stock_quantity':{'write_only': True},
            'image':{'required':False}
        }