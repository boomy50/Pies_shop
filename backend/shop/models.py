#from django.db import models #возможно потребуется разкоментить
import email
from pyexpat import model
from django.conf import settings
from django.db import models
from django.utils import timezone


###Модель продуктов###
class Products(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage_count = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=50)
    product_img = models.URLField()
    description = models.TextField()


###Модель пользователя###
#class User(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # phone = models.PositiveSmallIntegerField()#конкретизировать номер через+7
    # email = models.EmailField(blank=True)
    # password = models.CharField(max_length=100)#проверка  пароля ? 


###Модель заказа###
class Orders(models.Model):
    date = models.DateTimeField(default=timezone.now)
    adress = models.CharField(max_length=100, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


###Модель ингридиентов###
class Ingredients(models.Model):    
    ingredients_name = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage_count = models.PositiveSmallIntegerField()


###Промежуточная таблица###
class Order_products(models.Model):
    id_order = models.IntegerField()
    id_product = models.IntegerField()