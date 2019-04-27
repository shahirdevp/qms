from rest_framework import serializers
from mr.models import *

class DocTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = doc_type
        fields = ('id', 'doc_type_name')

class InterExternSerializer(serializers.ModelSerializer):
    class Meta:
        model = internal_external
        fields = ('id', 'doc_number', 'doc_name', 'doc_type', 'rev_no', 'date', 'doc_status', 'owner', 'creadedOn', )

class InternalAuditPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = internal_audit_plan
        fields = ('id', 'area_of_audit', 'auditee', 'auditor', 'as_clauses', 'year', 'month', 'status', 'owner', 'creadedOn', )


class InternalAuditReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = internal_audit_report
        fields = ('id', 'area_of_audit', 'audit_check_point', 'observations', 'owner', )



class NonConfSerializer(serializers.ModelSerializer):
    class Meta:
        model = non_conf_report
        fields = ('id', 'area_of_audit', 'ncr_no', 'nc_statement', 'objective_evidence', 'root_cause', 'containment_action', 'correction', 'correction_action', 'owner', 'creadedOn', )