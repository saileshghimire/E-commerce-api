from product.models import Category, Product, Comment, Review
from rest_framework import serializers


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

        