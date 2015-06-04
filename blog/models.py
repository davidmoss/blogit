from django.db import models

from picklefield.fields import PickledObjectField


class Blog(models.Model):
    name = models.CharField(max_length=60, default='blogit', unique=True)
    post_ids = PickledObjectField()


class Post(models.Model):
    title = models.CharField(max_length=60)
    synopsis = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    comment_ids = PickledObjectField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-created"]


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

from .receivers import *
