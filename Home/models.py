from django.db import models

# Create your models here.

class Post(models.Model):
    post_img = models.URLField()
    tag =  models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_img = models.URLField()
    user_name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
