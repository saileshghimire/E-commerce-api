from rest_framework import serializers
from product.models import Category

# class SubCategoryForCategoryListSerializer(serializers.ModelSerializer):
#     class Meta:
        

class CategoryListSerializer(serializers.ModelSerializer):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent_category']

    def get_parent_category(self,obj):
        if obj.parent_category:
            return CategoryListSerializer(obj.parent_category).data
        return None
    
class CategotyDetailSerializer(serializers.ModelSerializer):
    parent_category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), required =False)

    class Meta:
        model = Category
        fields = ['id','name', 'description', 'parent_category']

