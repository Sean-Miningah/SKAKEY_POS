from rest_framework import serializers
from .models import Shop, ShopProduct


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopProduct
        fields = '__all__'
