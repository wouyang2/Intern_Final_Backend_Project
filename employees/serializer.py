from rest_framework import serializers
from .models import Employee, Performance
from attendance.models import Attendance
from departments.models import Department


# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    Department = serializers.SlugRelatedField(slug_field = 'Name',read_only= True, source = 'Dept')
    class Meta:
        model = Employee
        fields = ['id', 'Name', 'Phone_Number', 'Email', 'Address', 'Date_of_join', 'Department']


# class AttendanceSerializer(serializers.ModelSerializer):

#     Name = serializers.SlugRelatedField(read_only=True, slug_field = 'Name')
#     class Meta:
#         model = Attendance
#         fields = ['id', 'Name', 'Date', 'Status']

class PerformanceSerializer(serializers.ModelSerializer):

    Name = serializers.SlugRelatedField(slug_field = 'Name',read_only=True)
    class Meta:
        model = Performance
        fields = '__all__'