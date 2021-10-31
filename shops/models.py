from django.db import models
from users.models import RetailerInfo

# Create your models here.


class Shop(models.Model):
    retailer_id = models.ForeignKey(RetailerInfo, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='user/shop/')


class ShopProduct(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=50, blank=False)
    quantity = models.FloatField(editable=True)
    price = models.BigIntegerField(editable=True)
    defination = models.TextField(max_length=250, blank=False)
    category = models.CharField(max_length=50, blank=False)
    source = models.CharField(max_length=50, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    image_1 = models.ImageField(upload_to='user/ShopProduct/', blank=False)
    image_2 = models.ImageField(upload_to='user/ShopProduct/', blank=True)
    image_3 = models.ImageField(upload_to='user/ShopProduct/', blank=True)
    image_4 = models.ImageField(upload_to='user/ShopProduct/', blank=True)
