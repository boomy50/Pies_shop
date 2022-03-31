#from django.db import models #возможно потребуется разкоментить

from pyexpat import model
from django.conf import settings
from django.db import models
from django.utils import timezone


class Products(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage_count = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=50)
    product_img = models.URLField()
    description = models.TextField()