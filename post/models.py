from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)#auto_now_add=True 只记录更新时间,不会改变
    updated = models.DateTimeField(auto_now=True)#auto_now=True 会随着表变化更新
    content = models.TextField()





