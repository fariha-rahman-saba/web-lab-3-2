from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=100, unique=True)
    emp_name = models.CharField(max_length=50)
    dept = models. CharField(max_length=150)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.emp_name} reg {self.emp_id}'


class Department(models.Model):
    dept = models.CharField(max_length=255)

    def __str__(self):
        return self.dept
