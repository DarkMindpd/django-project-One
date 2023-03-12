from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    user_img = models.URLField(default='https://s26.picofile.com/file/8460931518/user_3_.png')
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=100)
    born = models.DateField()
    date_of_singup = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    post_img = models.URLField()
    tag =  models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={"pk":self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    