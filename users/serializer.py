from rest_framework import serializers
from .models import RetailerInfo


class RetailerInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RetailerInfo
        fields = '__all__'
