from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView
)

from .forms import CommentForm, PostForm
from .mixins import AjaxableResponseMixin, PostSideNavMixin
from .models import Comment, Post


class PostCreateView(PostSideNavMixin, CreateView):
    http_method_names = ['get', 'post']
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('blog:post_list')
    template_name = 'create.html'


class PostListView(PostSideNavMixin, ListView):
    http_method_names = ['get']
    context_object_name = 'posts'
    model = Post
    paginate_by = 5
    template_name = 'list.html'

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
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
        context.update({
            'form': CommentForm(),
            'comments': Comment.objects.filter(post=self.get_object()),
        })
        return super(PostDetailView, self).get_context_data(**context)


class PostDeleteView(PostSideNavMixin, DeleteView):
    http_method_names = ['get', 'post']
    model = Post
    slug_field = 'id'
    success_url = reverse_lazy('blog:post_list')
    template_name = 'delete.html'


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
