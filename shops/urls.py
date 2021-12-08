from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
<<<<<<< HEAD
router.register(r'create-shop', views.ShopViewSet)
router.register(r'products', views.ShopProductViewSet)
=======
router.register(r'create-shops', views.ShopViewSet)
router.register(r'add_category', views.ProductCategoryViewSet)
router.register(r'cart', views.ShopCartViewSet)
router.register(r'add-products', views.ShopProductViewSet)
>>>>>>> create-shop

urlpatterns = [
    path('', include(router.urls)),
]
