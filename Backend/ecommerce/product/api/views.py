from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Product
from product.api.serializers import ProductSerializer

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

        


