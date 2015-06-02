from django.contrib.auth import logout
from django.shortcuts import redirect

from djangae.contrib.gauth.views import login_redirect


def login_view(request):
    return login_redirect(request)


def logout_view(request):
    logout(request)
    response = redirect('blog:post_list')
    response.delete_cookie('dev_appserver_login')
    return response
