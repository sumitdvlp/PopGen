from django.contrib.auth.models import User,Group
from .models import Job,JobFinal

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
	#extra_kwargs = {'user': {'required': False}}

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobFinal

        fields = ('id', 'job_status', 'op_file_url')

        #fields = ('id','user', 'job_name', 'op_file_url')

