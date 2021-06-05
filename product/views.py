from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Product, ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Product.objects.all().delete()
        return JsonResponse({'message': '{} Products were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    # find product by pk (id)
    product = Product.objects.get(pk=pk)
    if request.method == 'GET': 
        product_serializer = ProductSerializer(product) 
        return JsonResponse(product_serializer.data) 
    elif request.method == 'PUT': 
        product_data = JSONParser().parse(request) 
        product_serializer = ProductSerializer(product, data=product_data) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JsonResponse(product_serializer.data) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        product.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
