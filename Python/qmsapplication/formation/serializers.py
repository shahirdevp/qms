from rest_framework import serializers
from .models import  Cmp_formation
from django.contrib.auth.models import User


class CformationSerializer(serializers.ModelSerializer):
    ceo = serializers.CharField(source = 'User.username', read_only=True)
    class Meta:
        model = Cmp_formation
        fields = ( 'id', 'CmpName', 'scope', 'policy', 'app_domain', 'SupUser', 'ceo')