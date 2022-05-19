from rest_framework import serializers

from employees.models import employees
from home.models import department


class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ['department_id','name','age','avatar','cv']

