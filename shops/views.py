from rest_framework import viewsets
from .models import Shop, ShopProduct, ShopCategory, ShopCart
from .serializer import ShopSerializer, ShopProductSerializer, ShopCartSerializer, ShopCategorySerializer

# Create your views here.


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopProductViewSet(viewsets.ModelViewSet):
    queryset = ShopProduct.objects.all()
    serializer_class = ShopProductSerializer


class ShopCartViewSet(viewsets.ModelViewSet):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer


class ShopCategoryViewSet(viewsets.ModelViewSet):
    queryset = ShopCategory.objects.all()
    serailizer_class = ShopCategorySerializer
