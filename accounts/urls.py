from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path ( 'signup/', sign_up, name='signup' ),
    path ( 'signin/', sign_in, name='signin' ),
    path ( 'signout/', sign_out, name='signout' ),

    path (
        'password/change/',
        auth_views.PasswordChangeView.as_view (
            template_name='Authentication/password_change.html',
            success_url='/password/change/done/',
        ),
        name='password_change',
    ),
    path (
        'password/change/done/',
        auth_views.PasswordChangeDoneView.as_view (
            template_name='Authentication/password_change_done.html'
        ),
        name='password_change_done',
    ),
    path ( '', home, name='home' )
]