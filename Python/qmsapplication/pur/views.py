from pur.models import*
from pur.serializers import *
from rest_framework import mixins, generics


class Supplier(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset  = supplier.objects.all()
    serializer_class = SupplierSerialiser

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


class PurchaseApprovedSupplier(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset  = pur_approved_supplier.objects.all()
    serializer_class = ApproverdSupplierSerialiser

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


class PurchaseOrder(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset  = pur_supplier_purchase_order.objects.all()
    serializer_class = SpurOrderSerialiser

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


class GoodsRecipt(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset  = pur_goods_receipt_register.objects.all()
    serializer_class = GoodsResiptSerialiser

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


class StockRegister(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    queryset  = stock_register.objects.all()
    serializer_class = StockRegisterSerialiser

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