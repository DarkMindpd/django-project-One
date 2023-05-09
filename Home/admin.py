from django.contrib import admin
from accounts.models import User_profile
# Register your models here.

from post.models import Post,Comment
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User_profile)