from django.conf.urls import url, include
from rest_framework import routers

from . import views
from . import api

router = routers.DefaultRouter()
router.register(r'comment', api.CommentViewSet)
router.register(r'post', api.PostViewSet)

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^(?P<slug>[-\w]+)/comment/$', views.CommentCreateView.as_view(), name='add_comment'),
    url(r'^(?P<post>[-\w]+)/comment/(?P<slug>[-\w]+)/delete/$', views.CommentDeleteView.as_view(), name='delete_comment'),
]
