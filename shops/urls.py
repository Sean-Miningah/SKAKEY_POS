from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'create-shop', views.ShopViewSet)
router.register(r'products', views.ShopProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
