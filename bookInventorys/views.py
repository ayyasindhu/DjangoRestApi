from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from bookInventorys.models import BookInventory
from bookInventorys.serializers import BookInventorySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def bookInventory_list(request):
    if request.method == 'GET':
        bookInventorys = BookInventory.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            bookInventorys = bookInventorys.filter(title__icontains=title)
        
        bookInventorys_serializer = BookInventorySerializer(bookInventorys, many=True)
        return JsonResponse(bookInventorys_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        bookInventory_data = JSONParser().parse(request)
        bookInventory_serializer = BookInventorySerializer(data=bookInventory_data)
        if bookInventory_serializer.is_valid():
            bookInventory_serializer.save()
            return JsonResponse(bookInventory_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bookInventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = BookInventory.objects.all().delete()
        return JsonResponse({'message': '{} BookInventorys were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def bookInventory_detail(request, pk):
    try: 
        bookInventory = BookInventory.objects.get(pk=pk) 
    except BookInventory.DoesNotExist: 
        return JsonResponse({'message': 'The bookInventory does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bookInventory_serializer = BookInventorySerializer(bookInventory) 
        return JsonResponse(bookInventory_serializer.data) 
 
    elif request.method == 'PUT': 
        bookInventory_data = JSONParser().parse(request) 
        bookInventory_serializer = BookInventorySerializer(bookInventory, data=bookInventory_data) 
        if bookInventory_serializer.is_valid(): 
            bookInventory_serializer.save() 
            return JsonResponse(bookInventory_serializer.data) 
        return JsonResponse(bookInventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bookInventory.delete() 
        return JsonResponse({'message': 'BookInventory was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def bookInventory_list_published(request):
    bookInventorys = BookInventory.objects.filter(published=True)
        
    if request.method == 'GET': 
        bookInventorys_serializer = BookInventorySerializer(bookInventorys, many=True)
        return JsonResponse(bookInventorys_serializer.data, safe=False)
    
