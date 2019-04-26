from rest_framework import serializers
from pur.models import *

class SupplierSerialiser(serializers.ModelSerializer):
    class Meta:
        model = supplier
        fields = ( 'supplier', 'country', 'state', 'city', 'street', 'pin', 'phone', 'email', 'website', 'createdOn', )


class ApproverdSupplierSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pur_approved_supplier
        fields = ( 'date_entered', 'supplier', 'scope', 'status', 'next_approved_date', )


class SpurOrderSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pur_supplier_purchase_order
        fields = ( 'supplier', 'product', 'unit', 'supplier_ref_no', 'qty', 'po_no', 'po_date', 'requested_date', )


class GoodsResiptSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pur_goods_receipt_register
        fields = ( 'grrno', 'date', 'supplier', 'dc_ref', 'po_ref', 'part', 'inward_qty', 'sup_test_report', 'heat_lot_no', 'lenght', 'Hieght', 'width', 'diameter', 'accepted_qty', 'rej_qty', 'return_dc', 'date', )


class StockRegisterSerialiser(serializers.ModelSerializer):
    class Meta:
        model = stock_register
        fields = ( 'part_no', 'description', 'doc_ref', 'detail', 'recipt', 'issue', 'balance', 'date', )


