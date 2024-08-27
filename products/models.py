from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
import re

class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=10, unique=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clicked = models.PositiveIntegerField(default=0)
    hashtag = models.ManyToManyField(HashTag, related_name='hashtag_product', blank=True)

    def created_string(self):
        time = timezone.now() - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = timezone.now().date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
    
    def convert_hashtags_to_links(self):
        return re.sub(r'#(\w+)', r'<a class="hashtag" href="/products/hashtag/\1/">#\1</a>', self.content)

    def save_hash(self):
        hashtags = re.findall(r'#(\w+)', self.content)
        for tag in hashtags:
            hashtag, _ = HashTag.objects.get_or_create(hashtag_name=tag)
            self.hashtag.add(hashtag)
        return False


class Comment(models.Model):
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_user")
    comment_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comment_product")
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)