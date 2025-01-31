from django.db import models

# Create your models here.
class Teacher(models.Model):
    ni = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    phone  = models.CharField(max_length = 255)
    ocupacao = models.FloatField()