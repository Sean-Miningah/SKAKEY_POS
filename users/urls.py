from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'retailerinfo', views.RetailerInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
