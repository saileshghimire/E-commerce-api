from ..models import Review
from rest_framework import serializers

class ReviewListSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Review.objects.all())
    class Meta:
        model = Review
        fields = ['id','rating','product']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(**validated_data)