from rest_framework import serializers
from .models import Shop, ShopProduct, ShopCart, ShopCategory


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


class ShopCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopCategory
        fields = '__all__'
