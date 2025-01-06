from django.contrib.auth.models import User
from rest_framework import serializers
from .generate_uuid import generate_uuid
from .models import CustomUser

        
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # password is required but write-only

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password']  # Define the fields explicitly
        extra_kwargs = {
            'password': {'write_only': True},
            'middle_name': {'required': False} 
        }

    def create(self, validated_data):
        username = f"{validated_data['first_name']}{generate_uuid()}{validated_data['last_name']}"
        user = CustomUser.objects.create_user(**validated_data, username= username) 
        return user

class LoginSerializer(serializers.Serializer):
    email =serializers.EmailField()
    password = serializers.CharField()

