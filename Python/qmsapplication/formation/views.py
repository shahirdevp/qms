from rest_framework import mixins, generics
from .models import Cmp_formation
from .serializers import *

class CformationViewset(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset  = Cmp_formation.objects.all()
    serializer_class = CformationSerializer

    def get(self, request, pk=None):
        if pk:
            return  self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
