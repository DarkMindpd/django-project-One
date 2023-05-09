from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    post_img = forms.FileField()
    post_img = forms.ImageField()
    title = forms.CharField(max_length=255)
    body = forms.CharField()
    class Meta:
        model = Post
        fields = '__all__'