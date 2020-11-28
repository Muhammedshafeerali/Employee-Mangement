from django.db import models

# Create your models here.

class Employee(models.Model):
    
    employee_name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.BigIntegerField()
    adress=models.TextField(max_length=1000,verbose_name='description')
    image=models.ImageField(null=True ,blank=True)
