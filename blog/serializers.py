from rest_framework import serializers

from .models import Comment, Post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'created', 'author', 'body', 'post')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'synopsis', 'body', 'created')
