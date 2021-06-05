from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Category, CategorySerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET', 'POST', 'DELETE'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(category_serializer.data, safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(category_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Category.objects.all().delete()
        return JsonResponse({'message': '{} Categories were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    # find product by pk (id)
    category = Category.objects.get(pk=pk)
    if request.method == 'GET': 
        category_serializer = CategorySerializer(category) 
        return JsonResponse(category_serializer.data) 
    elif request.method == 'PUT': 
        category_data = JSONParser().parse(request) 
        category_serializer = CategorySerializer(category, data=category_data) 
        if category_serializer.is_valid(): 
            category_serializer.save() 
            return JsonResponse(category_serializer.data) 
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        category.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
