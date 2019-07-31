from django.shortcuts import render
from employee.models import Department,Employee,Salary
from employee.serializers import DepartmentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def department(request):
    if request.method=='GET':
        depart=Department.objects.all()
        departserializer=DepartmentSerializer(depart,many=True)
        return Response(departserializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        departserializer=DepartmentSerializer(data=request.data)
        if departserializer.is_valid():
            departserializer.save()
            return Response(departserializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(departserializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT','GET','DELETE'])
def department_detail(request,id):
    instance=get_object_or_404(Department,dept_no=id)
    if request.method=='GET':
        departserializer=DepartmentSerializer(instance)
        return Response(departserializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        departserializer=DepartmentSerializer(instance,data=request.data,partial=True)
        if departserializer.is_valid():
            departserializer.save()
            return Response(departserializer.data,status=status.HTTP_200_OK)
        else:
            return Response(departserializer.errors,status=status.HTTP_400_BAD_REQUEST)


