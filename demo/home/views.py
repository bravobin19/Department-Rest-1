from django.shortcuts import render

from rest_framework import generics
from rest_framework import filters
from home.models import department
from home.serializers import departmentSerializer
from rest_framework.permissions import IsAdminUser


class departmentlist(generics.ListAPIView):
    queryset = department.objects.all()
    serializer_class = departmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['department_id', 'name']
    permissions_classes = [IsAdminUser]

class departmentcreate(generics.CreateAPIView):
    queryset = department.objects.all()
    serializer_class = departmentSerializer
    permissions_classes = [IsAdminUser]

class departmentdestroy(generics.DestroyAPIView):
    queryset = department.objects.all()
    serializer_class = departmentSerializer
    permissions_classes = [IsAdminUser]


# class departmentListView(generics.ListAPIView):
#     queryset = department.objects.all()
#     serializer_class = departmentSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['department_id', 'name']
