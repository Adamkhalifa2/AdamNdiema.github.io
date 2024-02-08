from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()

class ImageYangu(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    product_image = models.ImageField(upload_to='images/')
