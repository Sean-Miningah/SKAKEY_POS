from rest_framework import viewsets

from .models import RetailerInfo, Shop
from .serializer import RetailerInfoSerializer, ShopSerializer

# Create your views here.


class RetailerInfoViewSet(viewsets.ModelViewSet):
    queryset = RetailerInfo.objects.all().order_by('-registration_date')
    serializer_class = RetailerInfoSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
