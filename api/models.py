from django.db import models

# Create your models here.
class Product(models.Model):
    """ 
    Product Model that represents a product in the store
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    end_date = models.DateField()