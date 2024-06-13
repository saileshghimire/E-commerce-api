from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Product, Comment, Review
from product.api.serializers import ProductSerializer, CommentSerializer, ReviewSerializer

class Productlist(APIView):

    def get(self,request):
        items = Product.objects.all()
        serializer = ProductSerializer(items,many=True)
        return Response(serializer.data)
    
    def post(self,request,fromat=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ProductEdit(APIView):
    
    def get(self,request,pk):
        try:
            items = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        seriallizer = ProductSerializer(items)
        return Response(seriallizer.data)
    
    def put(self,request,pk):
        items = Product.objects.get(pk=pk)
        serializer = ProductSerializer(items,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        items = Product.objects.get(pk=pk)
        items.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)


class Commentlist(APIView):

    def get(self,request):
        items = Comment.objects.all()
        serializer = CommentSerializer(items,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        



class CommentEdit(APIView):
    
    def get(self,request,pk):
        try:
            items = Comment.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        seriallizer = CommentSerializer(items)
        return Response(seriallizer.data)
    
    def put(self,request,pk):
        items = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(items,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        items = Comment.objects.get(pk=pk)
        items.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


class Reviewlist(APIView):

    def get(self,request):
        items = Review.objects.all()
        serializer = ReviewSerializer(items,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ReviewEdit(APIView):
    
    def get(self,request,pk):
        try:
            items = Review.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        seriallizer = ReviewSerializer(items)
        return Response(seriallizer.data)
    
    def put(self,request,pk):
        items = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(items,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        items = Review.objects.get(pk=pk)
        items.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)