from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView
)
from django.utils.translation import ugettext as _

from .forms import CommentForm, PostForm
from .mixins import AjaxableResponseMixin, PostSideNavMixin
from .models import Blog, Comment, Post


class PostCreateView(PostSideNavMixin, CreateView):
    http_method_names = ['get', 'post']
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('blog:post_list')
    template_name = 'create.html'

    def form_valid(self, form):
        response = super(PostCreateView, self).form_valid(form)
        messages.success(self.request, _('Post successfully created'))
        return response


class PostListView(PostSideNavMixin, ListView):
    http_method_names = ['get']
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'list.html'

    def get_queryset(self):
        blog, __ = Blog.objects.get_or_create(name='blogit')
        queryset = Post.objects.filter(pk__in=blog.post_ids)
        post_filter = self.request.GET.get('post_filter')
        if post_filter:
            month, year = post_filter.split('_')
            queryset.filter(created__month=month, created__year=year)
        return queryset


class PostDetailView(PostSideNavMixin, DetailView):
    http_method_names = ['get']
    model = Post
    slug_field = 'id'
    template_name = 'detail.html'

    def get_context_data(self, **context):
        post = self.get_object()
        context.update({
            'form': CommentForm(),
            'comments': Comment.objects.filter(
                post=self.get_object(),
                pk__in=post.comment_ids,
            ),
        })
        return super(PostDetailView, self).get_context_data(**context)


class PostDeleteView(PostSideNavMixin, DeleteView):
    http_method_names = ['get', 'post']
    model = Post
    slug_field = 'id'
    success_url = reverse_lazy('blog:post_list')
    template_name = 'delete.html'

    def delete(self, request, *args, **kwargs):
        response = super(PostDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, _('Post successfully deleted'))
        return response


class CommentCreateView(PostSideNavMixin, AjaxableResponseMixin, CreateView):
    http_method_names = ['post']
    fields = ['body']
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        post_id = self.kwargs.get('slug')
        return reverse_lazy('blog:post_detail', kwargs={'slug': post_id})

    def form_valid(self, form):
        post_id = self.kwargs.get('slug')
        post = form.save(commit=False)
        post.post = Post.objects.get(id=post_id)
        post.save()

        messages.success(self.request, _('Comment successfully created'))

        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return HttpResponseRedirect(self.get_success_url())


class CommentDeleteView(PostSideNavMixin, DeleteView):
    http_method_names = ['get', 'post']
    model = Comment
    slug_field = 'id'
    success_url = reverse_lazy('blog:post_list')
    template_name = 'delete_comment.html'

    def get_success_url(self):
        post_id = self.kwargs.get('post')
        return reverse_lazy('blog:post_detail', kwargs={'slug': post_id})

    def delete(self, request, *args, **kwargs):
        response = super(CommentDeleteView, self).delete(request,
                                                         *args, **kwargs)
        messages.success(self.request, _('Comment successfully deleted'))
        return response
