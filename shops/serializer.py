from rest_framework import serializers
from .models import Shop, ShopProduct, ShopCart, ProductCategory


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(), many=False)
    shop = serializers.PrimaryKeyRelatedField(
        queryset=Shop.objects.all(), many=False)

    class Meta:
        model = ShopProduct
        fields = (
            'id',
            'shop',
            'name',
            'category',
            'price',
            'quantity',
            'defination',
            'source',
            'photo',
            'barcode'
        )


class ShopCartSerializer(serializers.HyperlinkedModelSerializer):
    cart_products = serializers.PrimaryKeyRelatedField(
        queryset=ShopProduct.objects.all(), many=True
    )

    class Meta:
        model = ShopCart
        fields = (
            'id',
            'cart_products',
            'total_price',
            'mode_of_payment'
        )


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    shop = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all(),
                                              many=False)

    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'category',
            'description',
            'shop'
        )
