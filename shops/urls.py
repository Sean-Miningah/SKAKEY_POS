from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'create-shops', views.ShopViewSet, basename="create-shop")
router.register(r'add_category', views.ProductCategoryViewSet)
router.register(r'cart', views.ShopCartViewSet)
router.register(r'add-products', views.ShopProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
