from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    post_img = models.ImageField(upload_to='post_img', default='post_img/post_default.png')
    tags =  models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, default='')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True, related_name="likes", symmetrical=False)

    def get_absolute_url(self):
        return reverse('post', kwargs={"pk":self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

