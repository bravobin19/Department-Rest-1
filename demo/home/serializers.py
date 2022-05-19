from rest_framework import serializers

from home.models import department


class departmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = department
        fields =['name']