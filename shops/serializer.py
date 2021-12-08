from rest_framework import serializers
from .models import Shop, ShopProduct, ShopCart, ProductCategory


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopProduct
        fields = '__all__'


class ShopCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopCart
        fields = '__all__'


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
