from rest_framework import filters
from rest_framework import generics
from employees.models import employees
from employees.serializers import employeesSerializer
from home.models import department
from home.serializers import departmentSerializer
from rest_framework.permissions import IsAdminUser


class employeeslist(generics.ListAPIView):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permissions_classes = [IsAdminUser]


class employeescreate(generics.CreateAPIView):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer
    permissions_classes = [IsAdminUser]

class employeesupdate(generics.UpdateAPIView):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer
    permissions_classes = [IsAdminUser]

class employeesdelete(generics.DestroyAPIView):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer
    permissions_classes = [IsAdminUser]

# class employeessearch(generics.ListAPIView):
#     queryset = employees.objects.all()
#     serializer_class = employeesSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name']