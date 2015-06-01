from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.utils.translation import ugettext as _


def login_view(request):
    user = None
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            # Show error notification
            messages.error(request, _('User account is disabled'))
    else:
        # Show error notification
        messages.error(request, _('User and password details are incorrect'))
    return redirect('blog:post_list')


def logout_view(request):
    logout(request)
    response = redirect('blog:post_list')
    response.delete_cookie('dev_appserver_login')
    return response
