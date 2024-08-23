from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product

# Create your models here.
class User(AbstractUser):
    product_like = models.ManyToManyField(Product, related_name='user_like')