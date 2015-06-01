from rest_framework import viewsets

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or deleted.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or deleted.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
