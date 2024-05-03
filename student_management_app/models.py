from django.db import models

class Registration(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    username=models.TextField(max_length=50)
    Email=models.TextField(max_length=200)
    Password=models.TextField(max_length=12)

class Department(models.Model):
    Dept_Name=models.CharField(max_length=50)
    Description=models.TextField(max_length=120)

class Position(models.Model):
    Pos_Name=models.CharField(max_length=50)
    Description=models.TextField(max_length=150)

class Employee(models.Model):
    Dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    Emp_Name=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Address=models.TextField(max_length=250)
    Mobileno=models.TextField(max_length=12)
    Salary=models.IntegerField()
    Age=models.IntegerField()
    Email=models.TextField(max_length=200)
    Date_Of_Birth=models.DateTimeField()
    password=models.TextField(max_length=25)
  

class Attandance(models.Model):
    Emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Check_in=models.DateTimeField(null=True)
    Check_Out=models.DateTimeField(null=True)
    status=models.CharField(max_length=50)
class Leave(models.Model):
    Emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Reason=models.CharField(max_length=200)
    Start_Date=models.DateField()
    End_Date=models.DateField()
    status=models.CharField(max_length=20,default='pending')
   

class Task(models.Model):
    Emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Task_Name=models.CharField(max_length=80)
    Description=models.TextField(max_length=200)
    Start_Date=models.DateField()
    End_Date=models.DateField()
    status=models.CharField(max_length=20,default='pending')
   
class Notice(models.Model):
    Notice_Name=models.CharField(max_length=200)
    Description=models.TextField(max_length=200)

class Naitik(models.Model):
    first_Name=models.CharField(max_length=50)