from django.db import models
from django.conf import settings


# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profiles")
    image = models.ImageField(upload_to="images/", blank=True, null=True)

