from django.db import models
from datetime import datetime


class Post(models.Model):

    title = models.CharField(max_length=1024)
    text = models.CharField(max_length=8192)
    uuid = models.CharField(max_length=1024)
    votes = models.IntegerField()
    username = models.CharField(max_length=256)


class Comment(models.Model):
    username = models.CharField(max_length=256)
    text = models.CharField(max_length=8192)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    create_date = models.CharField(max_length=256, default=datetime.now())
