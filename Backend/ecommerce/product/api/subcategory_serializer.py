from product.models import Category, SubCategory
from rest_framework import serializers

class SubCategoryViewSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'description']

    def get_category(self, obj):
        return{
            'id':obj.category.id,
            'name':obj.category.name
        }

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = SubCategory
        fields = ['id','name','category', 'description']