from django.db import models
from users.models import RetailerInfo

# Create your models here.


class Shop(models.Model):
    retailer_id = models.ForeignKey(RetailerInfo, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='authentication/shop/')
