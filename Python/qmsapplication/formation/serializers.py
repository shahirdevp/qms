from rest_framework import serializers
from .models import  *
from django.contrib.auth.models import User


class CformationSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source= 'User.first_name' , read_only=True)
    policy = serializers.FileField(max_length=None, allow_empty_file=True, allow_null=True, required=False)
    class Meta:
        model = Cmp_formation
        fields = ( 'id', 'CmpName', 'scope', 'policy', 'app_domain', 'SupUser',  'Cunique')

class CprocessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ( 'id', 'CmpName', 'PrcName')
        
        

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create( username=validated_data['username'] )
        user.set_password(validated_data['password'])
        user.email(validated_data['email'])
        user.is_superuser = "1"
        user.save()
        # csuper = Cmp_formation.objects.create()
        # csuper = SupUser(user.id)
        # csuper.save()

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "password", "is_superuser", "email",)


class OrgProcessChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgProcessChart
        fields =('id', 'parentid', 'parent', 'child', 'orgName')


class OrgchartTest(serializers.ModelSerializer):
    class Meta:
        model = OrgTestprocess
        fields =('id', 'orgName', 'created_at', 'chart',)





