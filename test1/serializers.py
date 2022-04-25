from rest_framework import serializers
from . models import Project_create

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Project_create
