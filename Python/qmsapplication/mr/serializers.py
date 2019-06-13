from rest_framework import serializers
from mr.models import *


class DocTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = doc_type
        fields = ('id', 'doc_type_name')


class InterExternSerializer(serializers.ModelSerializer):
    class Meta:
        model = internal_external
        fields = ('id', 'doc_number', 'doc_name', 'doc_type', 'rev_no', 'date', 'doc_status', 'owner', 'creadedOn', 'type_of_doc')
        depth = 1


class InternalAuditPlanSerializer(serializers.ModelSerializer):
    # status = serializers.SerializerMethodField()
    class Meta:
        model = internal_audit_plan
        fields = ('id', 'area_of_audit', 'auditee', 'auditor', 'as_clauses', 'year', 'month', 'status', 'owner', 'creadedOn', )
        # read_only_fields = ('internal_audit_report')
    # def get_status(self,obj):
    #     return obj.get_status_display()


class InternalAuditPlanFrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = internal_audit_plan
        fields = ('area_of_audit',)


class InternalAuditReportSerializer(serializers.ModelSerializer):
    area_of_audit = InternalAuditPlanFrgSerializer('area_of_audit',)
    class Meta:
        model = internal_audit_report
        fields = ('id', 'area_of_audit', 'audit_check_point', 'observations', 'owner', )
        # depth = 1


class NonConfSerializer(serializers.ModelSerializer):
    class Meta:
        model = non_conf_report
        fields = ('id', 'area_of_audit', 'ncr_no', 'nc_statement', 'objective_evidence', 'root_cause', 'containment_action', 'correction', 'correction_action', 'creadedOn', )
        # depth = 1