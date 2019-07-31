from django.urls import path
from employee.views import department,department_detail

urlpatterns=[
    path('v1/api/department',department,name='document'),
    path('v1/api/department_detail/<str:id>',department_detail,name='department_detail')
]