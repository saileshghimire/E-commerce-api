from ..models import Comment, Product
from serializers import serializers
from user_app.models import CustomUser

class ProductForCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']

class UserForCommentListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'name']

    def get_name(self, obj):
        if obj.middle_name:
            return f"{obj.first_name} {obj.middle_name} {obj.last_name}"
        return f"{obj.first_name} {obj.last_name}"

class CommentListSerializer(serializers.ModelSerializer):
    Product = ProductForCommentListSerializer()
    user = UserForCommentListSerializer()
    class Meta:
        model = Comment
        fields = ['id','comment', 'product','user']



class CommentCreateSerializer(serializers.ModelSerializer):
    Product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = Comment
        fields = ['id','comment','product','user']
