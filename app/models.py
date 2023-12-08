from django.db import models

# Create your models here.
class Dept(models.Model):
    Dept_No=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    
class Emp(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Ejob=models.CharField(max_length=100)
    Mgid=models.IntegerField()
    Hiredate=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField()
    Dept_No=models.OneToOneField(Dept,on_delete=models.CASCADE)
    
class Salgrade(models.Model):
    Grade=models.IntegerField()
    Losal=models.IntegerField()
    Hisal=models.IntegerField()