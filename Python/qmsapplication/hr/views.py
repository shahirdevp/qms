from hr.models import *
from hr.serializers import *
from rest_framework import mixins
from rest_framework import generics

# hr list
class Hrlist(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = hr.objects.all()
    serializer_class = HrlistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class HrDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = hr.objects.all()
    serializer_class = HrlistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# employee 
class EmployeeView( mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset  = employe.objects.all()
    serializer_class = EmployeeSerializer

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
    
# experience
class ExpView( mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset  = experience.objects.all()
    serializer_class = ExperienceSerializer

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


# competency-matrix
class CompetencyView( mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset  = competency_Matrix.objects.all()
    serializer_class = CompetencySerializer

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

# training-request
class TrainingRequestView( mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset  = training_Request_Register.objects.all()
    serializer_class = TrainingReqSerializer

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


# annual-trainnig
class AnnualTrainnigView( mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset  = annual_trainnig.objects.all()
    serializer_class = AnualTrainingSerializer

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


# training-evalution
class TrainingEvalutionView( mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset  = training_evalution_record.objects.all()
    serializer_class = TeEvRecordSerializer

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