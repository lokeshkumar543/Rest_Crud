from dataclasses import Field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','selling_price','discount_price','discription','brand','product_image']