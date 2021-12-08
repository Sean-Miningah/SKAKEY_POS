from django.db import models

# Create your models here.


class Shop(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    shopname = models.CharField(max_length=20, blank=False)
    location = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='user/shop/')
    category = models.CharField(max_length=20, blank=False)


class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    quantity = models.FloatField(editable=True)
    price = models.BigIntegerField(editable=True)
    defination = models.TextField(max_length=250, blank=False)
    category = models.CharField(max_length=50, blank=False)
    source = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='Shop/ShopProduct/', blank=False)
    barcode = models.CharField(max_length=150, blank=True)


class ProductCategory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, blank=False)
    last_update = models.DateTimeField(auto_now=True)


class ShopCart(models.Model):
    MPESA = 'MPESA'
    CASH = 'CASH'
    CARD = 'SHOP-CARD'

    PAYMENT_CHOICES = [
        (MPESA, 'm-pesa'),
        (CASH, 'cash'),
        (CARD, 'shop-card')
    ]
    total_price = models.BigIntegerField(default=0, editable=False,)
    cart_products = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    mode_of_payment = models.CharField(max_length=10,
                                       choices=PAYMENT_CHOICES, blank=True)
