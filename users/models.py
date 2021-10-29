from django.db import models
from datetime import datetime

# Create your models here.


class RetailerInfo(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=25, null=False)
    government_id = models.CharField(max_length=25, null=False)
    second_contact_first_name = models.CharField(max_length=50, blank=True)
    second_contact_last_name = models.CharField(max_length=50, blank=True)
    second_contact_phone_number = models.CharField(max_length=25, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
