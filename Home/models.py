from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img', default='profile_img/user_default.png')
    bio = models.CharField(max_length=100, default="")
    born = models.DateField(default="")

class Post(models.Model):
    post_img = models.ImageField(upload_to='post_img', default='post_img/post_default.png')
    tag =  models.CharField(max_length=15, default='')
    title = models.CharField(max_length=255, default='')
    body = models.TextField()
    user_name = models.ForeignKey(User_profile,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={"pk":self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_name = models.ForeignKey(User_profile,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    