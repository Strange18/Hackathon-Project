from django.shortcuts import render
from home.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import idea_serializer


# basic CURD operations in rest framework

# Create operation
@api_view(['POST'])
def add_item(request):
    serializer = idea_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Read operation
@api_view(['GET'])
def view_items(request):
    item = idea.objects.all()
    serializer = idea_serializer(item, many=True)
    return Response(serializer.data)


# update operation
@api_view(['POST'])
def update_item(request, pk):
    item = idea.objects.get(id=pk)
    serializer = idea_serializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete operation
@api_view(['DELETE'])
def delete_item(request, pk):
    item = idea.objects.get(id=pk).delete()
    return Response("Item Deleted Successfully")

