from hr.models import hr
from .serializers import HrSerializer
from rest_framework import viewsets


class HrViewSet(viewsets.ModelViewSet):
    queryset = hr.objects.all()
    serializer_class = HrSerializer
