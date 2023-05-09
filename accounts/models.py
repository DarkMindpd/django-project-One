from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img', blank=True, null=True, default="profile_img/user_default2.png")
    user_phone_num = models.IntegerField(blank=True, null=True)
    user_company = models.CharField(max_length=100, default="", blank=True, null=True)
    user_designation = models.CharField(max_length=100, default="", blank=True, null=True)
    user_location = models.CharField(max_length=100, default="", blank=True, null=True)
    bio = models.CharField(max_length=100, default="", blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)

    def __str__(self) -> str:
        return self.user.username + ' |profile|'
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    try:
        instance.user_profile
    except:
        User_profile.objects.create(user=instance)