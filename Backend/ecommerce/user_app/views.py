from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login,logout


class RegisterView(generics.CreateAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class = CustomUserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            resposne={
                "message":"User registered Successfully"
            }
            return Response(resposne,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Loginview(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            print(f"user details:{user}")
            if user is not None:
                refresh_token = RefreshToken.for_user(user=user)
                access_token = refresh_token.access_token
                response = {
                    "access_token": str(access_token),
                    "refresh_token": str(refresh_token)
                }
                print(response)
                return Response(response, status=status.HTTP_200_OK)
            return Response({"message":"Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)