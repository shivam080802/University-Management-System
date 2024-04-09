from django.db import models

# Create your models here.

class Department(models.Model):
    
    department_name = models.CharField(max_length = 10)
    department_id = models.CharField(max_length=10, primary_key = True)
    def __str__(self):
        return self.department_name


class Student(models.Model):
    student_name = models.CharField(max_length = 20)
    student_id =models.CharField(max_length=10, primary_key = True)
    mobile_number = models.CharField(max_length=10)
    department_id = models.ForeignKey(Department, on_delete =models.CASCADE)
    aadhar_number = models.CharField(max_length = 12)
    email = models.EmailField()
    def __str__(self):
        return f"{self.student_id} : {self.student_name}"


class Faculty(models.Model):
    faculty_name = models.CharField(max_length = 20)
    faculty_id = models.CharField(max_length=10, primary_key = True)
    department_id = models.ForeignKey(Department, on_delete =models.CASCADE)
    faculty_mobile_number = models.CharField(max_length=10)
    faculty_email = models.EmailField()
    def __str__(self):
        return f"{self.faculty_id} : {self.faculty_name}"
 

