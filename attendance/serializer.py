from .models import Attendance
from rest_framework import serializers

class AttendanceSerializer(serializers.ModelSerializer):

    Name = serializers.SlugRelatedField(read_only=True, slug_field = 'Name')
    class Meta:
        model = Attendance
        fields = ['id', 'Name', 'Date', 'Status']