from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = 
    content = models.TextField()
