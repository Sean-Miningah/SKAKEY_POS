from rest_framework import viewsets

from .models import RetailerInfo
from .serializer import RetailerInfoSerializer

# Create your views here.


class RetailerInfoViewSet(viewsets.ModelViewSet):
    queryset = RetailerInfo.objects.all().order_by('-registration_date')
    serializer_class = RetailerInfoSerializer
