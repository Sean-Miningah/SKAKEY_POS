from rest_framework import viewsets
from .models import Shop, ShopProduct
from .serializer import ShopSerializer, ShopProductSerializer

# Create your views here.


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopProductViewSet(viewsets.ModelViewSet):
    query = ShopProduct.objects.all()
    serialiser_class = ShopProductSerializer
