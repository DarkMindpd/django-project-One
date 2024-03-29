from django import forms
from .models import Post, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_img','tags','title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
