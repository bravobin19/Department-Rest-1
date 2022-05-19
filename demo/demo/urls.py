"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import include, path

from employees.views import employeeslist, employeescreate, employeesupdate, employeesdelete

from home.views import departmentlist, departmentcreate, departmentdestroy

urlpatterns = [

    path('admin/', admin.site.urls),
    # Department
    path('', departmentlist.as_view()),
    path('create', departmentcreate.as_view()),
    path('delete/<pk>', departmentdestroy.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   # path('searchdepartment', departmentListView.as_view()),


    # Employees
    path('employees', employeeslist.as_view()),
    path('createemployees', employeescreate.as_view()),
    path('updateemployees/<pk>', employeesupdate.as_view()),
    path('deleteemployees/<pk>', employeesdelete.as_view()),
]
