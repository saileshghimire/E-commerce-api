from .review_serializer import ReviewListSerializer
from ..models import Review
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    