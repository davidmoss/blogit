from django.db import models

from .models import Blog, Comment, Post


def add_post_id(sender, instance, **kwargs):
    blog, __ = Blog.objects.get_or_create(name='blogit')
    if blog.post_ids:
        blog.post_ids.append(instance.id)
    else:
        blog.post_ids = [instance.id]
    blog.save()


def add_comment_id(sender, instance, **kwargs):
    post = instance.post
    if post.comment_ids:
        post.comment_ids.append(instance.id)
    else:
        post.comment_ids = [instance.id]
    post.save()


def remove_post_id(sender, instance, **kwargs):
    blog, __ = Blog.objects.get_or_create(name='blogit')
    if instance.id in blog.post_ids:
        blog.post_ids.remove(instance.id)
        blog.save()


def remove_comment_id(sender, instance, **kwargs):
    post = instance.post
    if instance.id in post.comment_ids:
        post.comment_ids.remove(instance.id)
        post.save()


models.signals.post_save.connect(add_post_id, sender=Post)
models.signals.post_save.connect(add_comment_id, sender=Comment)
models.signals.post_delete.connect(remove_post_id, sender=Post)
models.signals.post_delete.connect(remove_comment_id, sender=Comment)
