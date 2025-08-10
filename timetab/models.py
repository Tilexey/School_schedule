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
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    st_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    birth_date = models.DateField()
    
class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_room = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField()

    