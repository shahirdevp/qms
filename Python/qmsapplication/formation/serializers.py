from rest_framework import serializers
from .models import  *
from django.contrib.auth.models import User


class CformationSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source= 'User.first_name' , read_only=True)
    policy = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Cmp_formation
        fields = ( 'id', 'CmpName', 'scope', 'policy', 'app_domain', 'SupUser',  'Cunique')

class CprocessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ( 'id', 'CmpName', 'PrcName')
        