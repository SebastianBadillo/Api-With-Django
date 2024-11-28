from django.shortcuts import render
from rest_framework import viewsets
from .serial import ProductSerializer
from rest_framework.response import Response
from .models import Product
# Create your views here.
# Set of views for the CRUD model
class ProductViewSet(viewsets.ModelViewSet):
    """
    API-REST endpoint for car model, allows to perform CRUD operations
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer