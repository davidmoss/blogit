from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['coment_ids']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
