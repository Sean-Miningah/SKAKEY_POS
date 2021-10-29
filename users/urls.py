from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'retailerinfo', views.RetailerInfoViewSet)
router.register(r'shop', views.ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
