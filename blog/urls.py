from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers

from . import views
from . import api

router = routers.DefaultRouter()
router.register(r'comment', api.CommentViewSet)
router.register(r'post', api.PostViewSet)

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^create/$', login_required(views.PostCreateView.as_view()), name='post_create'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<slug>[-\w]+)/delete/$', login_required(views.PostDeleteView.as_view()), name='post_delete'),
    url(r'^(?P<slug>[-\w]+)/comment/$', login_required(views.CommentCreateView.as_view()), name='add_comment'),
    url(r'^(?P<post>[-\w]+)/comment/(?P<slug>[-\w]+)/delete/$', login_required(views.CommentDeleteView.as_view()), name='delete_comment'),
]
