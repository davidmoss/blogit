from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = []


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
