from django.db import models
from django.conf import settings
from datetime import datetime, timedelta

# class Free(models.Model):
#     @property
#     def created_string(self):
#         time = datetime.now(tz=timezone.utc) - self.registered_date

#         if time < timedelta(minutes=1):
#             return '방금 전'
#         elif time < timedelta(hours=1):
#             return str(int(time.seconds / 60)) + '분 전'
#         elif time < timedelta(days=1):
#             return str(int(time.seconds / 3600)) + '시간 전'
#         elif time < timedelta(days=7):
#             time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
#             return str(time.days) + '일 전'
#         else:
#             return False
class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=10, unique=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product")#r_n수정필요
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clicked = models.PositiveIntegerField(default=0)
    hashtag = models.ManyToManyField(HashTag, related_name='hashtag_product', blank=True)

class Comment(models.Model):
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_user")#r_n수정필요
    comment_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comment_product")#r_n수정필요
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)