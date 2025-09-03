from django.db import models
# Create your models here.

class Department(models.Model):
    Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Name