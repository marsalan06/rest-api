from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import products
from .serializers import productsserializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
#function based views
@api_view(['GET','POST'])
def products_list(request):
    if request.method == 'GET':
        obj=products.objects.all()
        serializer=productsserializer(obj, many=True)
        return Response(serializer.data)
    elif request.method== 'POST':
        serializer= productsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT'])       
def product_detail(request,pk):
    try:
        obj= products.objects.get(id= pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=productsserializer(obj)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=productsserializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

