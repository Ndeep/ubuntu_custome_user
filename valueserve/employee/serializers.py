from rest_framework import serializers
from employee.models import Department,Employee,Salary
from rest_framework.exceptions import ValidationError

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('dept_no','dept_name')

    def validate(self, attrs):
        print('valid')
        dept_no=attrs.get('dept_no','')
        dept_name=attrs.get('dept_name','')
        if len(dept_name)<3:
            raise ValidationError('Please mention full name.')
        if type(dept_no) ==type(1):
            raise ValidationError('Department number should be Varchar..')
        return attrs

    # def create(self, validated_data):
    #     print('New department {0} going to create'.format(validated_data['dept_name']))
    #     return Department.objects.create(**validated_data)


class EmployeeSerializer(serializers.ModelSerializer):
    pass