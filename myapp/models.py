from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('registrar', 'registrar'),
        ('admin', 'admin'),
    )
    roles=models.CharField(max_length=20,choices=ROLE_CHOICES,default='student')
    name=models.CharField(max_length=20,default="")
    def __str__(self):
        return f"{self.name} || ({self.roles})"
    fees_submitted=models.BooleanField(default=False)
    
class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department_choice=(
        ('Computer Science', 'Computer Science'),
        ('Electrical', 'Electrical'),
        ('Mechanical', 'Mechanical'),
        ('Electronics', 'Electronics'),
        ('B.Pharma', 'B.Pharm'),
        ('Biotech', 'Biotech'),
    )
    department=models.CharField(max_length=20,choices=department_choice)
    phone_num=models.CharField(max_length=15,default=0)
    salary_choice=(
       ( 30000,'₹30,000/month'),
       ( 40000,'₹40,000/month'),
       ( 50000,'₹50,000/month'),
    )
    salary_per_month=models.IntegerField(max_length=10,choices=salary_choice)
    section=models.CharField(max_length=20)
    subject = models.CharField(max_length=100,default="")
    def __str__(self):
        return f"{self.user.name}|| ({self.department.upper()})"


    
      
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    branch=models.CharField(max_length=30,blank=True,null=True)
    section=models.CharField(max_length=2,blank=True,null=True)
    attendance=models.FloatField(max_length=10,default=0.0)
    marks=models.FloatField(max_length=10,default=0.0)
    year=models.IntegerField(max_length=10,blank=True,default=True)
    fees_amount=models.IntegerField(max_length=20)
    receipt=models.FileField(upload_to='receipts',null=True,blank=True)
    registered=models.BooleanField(default=False)
    phone_num=models.CharField(max_length=15,default=0)
    def __str__(self):
        return f"{self.user.name}|| {self.section} || {self.branch}"

    
