from django.db import models

# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    image = models.ImageField()