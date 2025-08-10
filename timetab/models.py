from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
class Teacher(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
class Class(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    st_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    birth_date = models.DateField()
    