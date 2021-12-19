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
    firebase_token = models.CharField(max_length=50, blank=True)

    def __string__(self):
        return self.shopname


class ProductCategory(models.Model):
    # shop will be handled with session
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, blank=False)
    p_description = models.CharField(max_length=100, blank=False)
    last_update = models.DateTimeField(auto_now=True)

    def __string__(self):
        return self.category


class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    quantity = models.FloatField(editable=True)
    price = models.BigIntegerField(editable=True)
    prediction = models.TextField(max_length=250, blank=False)
    category = models.OneToOneField(
        ProductCategory, on_delete=models.CASCADE, blank=False)
    source = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='Shop/ShopProduct/', blank=True)
    barcode = models.CharField(max_length=150, blank=True)

    def __string__(self):
        return self.name

# shopping cart logic


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
