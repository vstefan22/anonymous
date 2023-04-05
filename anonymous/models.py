from django.db import models
from django.contrib.auth.models import User

class Anonymous(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_number = models.IntegerField()
    code = models.TextField()

class ID(models.Model):
    user_number = models.IntegerField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Tags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

class Comments(models.Model):
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

