from django.db import models

# Create your models here.
# Student Schemas
class Student(models.Model):
    #id=models.AutoField()--Automatically Added by Django, it is Primary key
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    #Profile_photo = models.ImageField()
    file = models.FileField()
    dob = models.DateField()


#Product Schemas
class product(models.Model):
    pass
 # product_name = models.CharField()