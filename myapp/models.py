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
        return f"{self.username} ({self.roles})"