from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from departments.models import Department
# Create your models here.

# class Department(models.Model):
#     Name = models.CharField(max_length=255)
#     def __str__(self):
#         return self.Name

class Employee (models.Model):
    Name = models.CharField(max_length = 255)
    Email = models.EmailField(max_length=255, unique=True)
    Phone_Number = PhoneNumberField(unique = True, blank= False)
    Address = models.CharField(max_length=255, null = True)
    Date_of_join = models.DateField(null= True)
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.Name


# class Attendance(models.Model):
#     Name = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     Date = models.DateField(null=True)
#     Status = models.CharField(max_length = 255)

class Performance(models.Model):
    Name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Review_date = models.DateField(null = True)