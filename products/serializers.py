from rest_framework import serializers
from .models import products


class productsserializer(serializers.ModelSerializer):
    class Meta:
        model= products
        fields = ('id','name','description','price')
        #if upper give assertion error , use  fields = ‘__all__’ or 
        #fields = (‘some’, ‘fields’,...), exclude = (‘fields’, ‘other’, ‘than’, ‘these’...)