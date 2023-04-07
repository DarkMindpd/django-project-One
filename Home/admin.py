from django.contrib import admin

# Register your models here.

from .models import Post,Comment,User_profile
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User_profile)