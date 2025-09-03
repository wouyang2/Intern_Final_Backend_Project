from django.shortcuts import render
from .serializer import DepartmentSerializer
from .models import Department
from rest_framework import viewsets, permissions

# Create your views here.
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]