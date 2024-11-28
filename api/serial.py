from rest_framework import serializers

# The model is imported from the models.py file
from .models import Product

# The ProductSerializer class is created to serialize the Product model
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Product
        fields = ['id', 'name', 'price', 'description', 'end_date']