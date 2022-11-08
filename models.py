from django.db import models

# Create your models here.
class DepartmentList(models.Model):
    DepName = models.CharField(max_length=100,null=False, blank=True)
    Description = models.CharField(max_length=100,null=True, blank=True)
    CreatedBy = models.CharField(max_length=100,null=True, blank=True)
    CreatedDateTime = models.CharField(max_length=100,null=True, blank=True)
    UpdatedBy = models.CharField(max_length=100,null=True, blank=True)
    UpdatedDateTime = models.CharField(max_length=100,null=True, blank=True)
    IsDeleted = models.CharField(max_length=100,null=True, blank=True)
    
class Employee(models.Model):
    EmpId = models.CharField(max_length=100, null=False, blank=True)
    Firstname = models.CharField(max_length=100, null=False, blank=True)
    LastName = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(max_length=100, null = False,blank=True)
    Password = models.TextField(max_length=100, null=False, blank=True)
    #DepartmentId = models.ForeignKey('DepartmentList', on_delete=models.CASCADE)
    #EmployeeTypeId = models.ForeignKey('EmployeeTypeList', on_delete=models.CASCADE)
    ReportTold = models.CharField(max_length=100, null=False, blank=True)
    CreatedById = models.CharField(max_length=100, null=False, blank=True)
    CreatedDateTime = models.CharField(max_length=100, null=False, blank=True)
    UpdatedById = models.CharField(max_length=100, null=False, blank=True)
    UpdatedDateTime = models.CharField(max_length=100, null=False, blank=True)
    IsDeleted = models.CharField(max_length=100, null=True, blank=True)

class Attendance(models.Model):
    EmpId = models.ForeignKey('Employee', on_delete=models.CASCADE)
    Longitude = models.CharField(max_length=100)
    Lattitude = models.CharField(max_length=100)
    AreaDescription = models.CharField(max_length=100)
    AttendanceDate = models.DateTimeField()
    AttendanceTime = models.DateTimeField()

class Login(models.Model):
    EmpId = models.ForeignKey("Employee",on_delete=models.CASCADE)
    Password = models.CharField(max_length=100,null=False, blank=True)
    LoginDateTime = models.CharField(max_length=100,null=False, blank=True)

class EmployeeTypeList(models.Model):
    TypeDescription = models.CharField(max_length=100,null=False, blank=True)
    CreatedBy = models.CharField(max_length=100,null=False, blank=True)
    CreatedDateTime = models.DateTimeField(max_length=100,null=False, blank=True)
    UpdatedById = models.CharField(max_length=100,null=False, blank=True)
    UpdatedDateTime = models.CharField(max_length=100,null=False, blank=True)
    IsDeleted = models.CharField(max_length=100,null=True, blank=True)
