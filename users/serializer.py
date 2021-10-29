from rest_framework import serializers
from .models import RetailerInfo, Shop


class RetailerInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RetailerInfo
        fields = '__all__'


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
