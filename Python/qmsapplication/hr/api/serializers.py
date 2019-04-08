from rest_framework import serializers
from hr.models import *


class HrSerializer(serializers.ModelSerializer):
    class Meta:
        model = hr
        fields = ('hr_required_deg', 'requestedby', 'reson_new_hire')

