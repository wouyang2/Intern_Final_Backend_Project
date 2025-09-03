from django.db import models
from employees.models import Employee
# Create your models here.


class Attendance(models.Model):
    Name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date = models.DateField(null=True)
    Status = models.CharField(max_length = 255)