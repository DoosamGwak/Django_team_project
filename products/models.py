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


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_user")
    comment_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comment_product")
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)