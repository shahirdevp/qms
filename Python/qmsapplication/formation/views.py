from rest_framework import mixins, generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import  FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User

class CreateUserView(generics.CreateAPIView):
    model = User()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class CformationViewset(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset = Cmp_formation.objects.all()
    serializer_class = CformationSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class CprocessViewset(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset  = Process.objects.all()
    serializer_class = CprocessSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class CprocessCmpViewset(generics.GenericAPIView,
                        mixins.ListModelMixin):
    lookup_field = 'CmpName'
    queryset  = Process.objects.all()
    serializer_class = CprocessSerializer

    def get(self, request, CmpName=None):
        return self.list(request, CmpName)


class PolicyViewset(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = CformationSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrgProcessChartViewset(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin):

    queryset = OrgTestprocess.objects.all()
    serializer_class = OrgchartTest

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        # print(request.data)
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

# meeting minuts
class MeetingMinutsViewset(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin):

    queryset = MeetingMinuts.objects.all()
    serializer_class = MeetingMinutsSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        # print(request.data)
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
