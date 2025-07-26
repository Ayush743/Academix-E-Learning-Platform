from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class Student(models.Model):
    ...
    profile = CloudinaryField('image', blank=True, null=True)

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('registrar', 'registrar'),
        ('admin', 'admin'),
    )
    roles=models.CharField(max_length=20,choices=ROLE_CHOICES,default='student')
    profile=CloudinaryField('profile',blank=True,null=True)
    name=models.CharField(max_length=20,default="")
    def __str__(self):
        return f"{self.name} || ({self.roles})"
    fees_submitted=models.BooleanField(default=False)
    
class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile=CloudinaryField('profile',blank=True,null=True)
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
    section=models.CharField(max_length=2,default="")
    attendance=models.FloatField(max_length=10,default=0.0)
    profile=CloudinaryField('profile',blank=True,null=True)
    marks=models.FloatField(max_length=10,default=0.0)
    year=models.IntegerField(max_length=10,blank=True,default=True)
    fees_amount=models.IntegerField(max_length=20)
    receipt=CloudinaryField('receipt',null=True,blank=True,resource_type='raw')
    registered=models.BooleanField(default=False)
    phone_num=models.CharField(max_length=15,default=0)
    def __str__(self):
        return f"{self.user.name}|| {self.section} || {self.branch}"

    
class Announcement(models.Model):
    title=models.CharField(max_length=200)
    roles=models.CharField(max_length=20,null=True,blank=True)
    desc=models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    branch=models.CharField(max_length=30,blank=True,null=True)
   
    section=models.CharField(max_length=2,blank=True,null=True)
    target_user=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='target_user')
    def __str__(self):
        return f"{self.title}||{self.created_by}"

class Assignment(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default="no title")
    desc=models.TextField()
    file=CloudinaryField('file',blank=True,null=True,resource_type='raw')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline= models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return f"{self.title}-{self.teacher.user.name}"
class Student_submission(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    assgn=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    subject=models.CharField(max_length=30,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file=CloudinaryField('file',blank=True,null=True,resource_type='raw')
    def __str__(self):
        return f"{self.title}-{self.student.user.name}"

class Notes(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default="no title")
    file=CloudinaryField('file',blank=True,null=True,resource_type='raw')
    message=models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.teacher.user.name}"


