from rest_framework import serializers
from marketing.models import *

class EnqRegisterSerialiser(serializers.ModelSerializer):
    class Meta:
        model = mtk_enquiry_register
        fields = ('id', 'customer', 'date', 'prodeliverDate', 'contact', 'contryCode', 'line_number','partNumber', 'description', 'drawingNumber', 'qty', 'quotationRef', 'status', 'poNumber', 'creadedOn', 'owner' )
        # extra_kwargs = {'owner': {'default': serializers.CurrentUserDefault()}}

class TecFeasSerialiser(serializers.ModelSerializer):
    class Meta:
        model = tech_feasibility
        fields = ( 'id', 'cusomer', 'r_mtrl', 'm_c', 'tools', 'Spl_process', 'any_cad_req', 'out_source', 'owner' )

class MktFeasSerialiser(serializers.ModelSerializer):
    class Meta:
        model = marketing_feasibility
        fields = ('id', 'cusomer', 'owner', 'is_statuatory_regulatory', 'is_delivery_feasibility', 'is_nre_applicable', 'creadedOn', )

class QltyFeasSerialiser(serializers.ModelSerializer):
    class Meta:
        model = quality_feasibility
        fields = ('id', 'cusomer' , 'owner' , 'inst' , 'gauge' , 'can_aql_be_achived' , 'is_fai_required' , 'key_chare' , 'ispection_as_per' , 'creadedOn' , )


class ReviewerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = reviewer
        fields = ('id', 'cusomer', 'owner', 'mkt', 'qcd', 'pur', 'prd', 'creadedOn', )



class ConfMRSerialiser(serializers.ModelSerializer):
    class Meta:
        model = configuration_management_report
        fields = ('id', 'cusomer', 'owner', 'creadedOn', 'customer_order', 'route_card_no', 'internal_job_order', 'rev_no', 'invoice_no', )

class customeListrerialiser(serializers.ModelSerializer):
    class Meta:
        model = mtk_enquiry_register
        fields = ('id', 'customer',)

# feasiblity study serializer

class feasDta(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    slno = serializers.FloatField(source='slNo')
    capability = serializers.CharField(source='company_capability')
    reqname = serializers.CharField(source='customer_requirement', required=False, allow_blank=True)
    reamarkname = serializers.CharField(source='remarks', required=False, allow_blank=True)
    class Meta:
        model = feasibility_study_list
        fields = ('slno', 'id', 'capability', 'reqname', 'reamarkname', )


class feasiblitySerializer(serializers.ModelSerializer):
    feasibility_study_list = feasDta(many=True)
    class Meta:
        model = feasibility_study
        fields = ('id', 'owner', 'createdOn', 'statutory', 'customer', 'feasibility_study_list')

    def create(self, validated_data):
        feasiblity_datas = validated_data.pop('feasibility_study_list')
        feasibility = feasibility_study.objects.create(**validated_data)
        for feasiblity_data in feasiblity_datas:
            feasibility_study_list.objects.create(**feasiblity_data, feasibility=feasibility)
        return feasibility
