from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'create-shops', views.ShopViewSet)
router.register(r'add_category', views.ShopCartViewSet)
router.register(r'category', views.ShopCartViewSet)
router.register(r'add-products', views.ShopProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
