from django.shortcuts import render
from .serializer import AttendanceSerializer
from .models import Attendance
from rest_framework import viewsets, permissions

class AttendanceViewset(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
