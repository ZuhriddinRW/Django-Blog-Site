from django.urls import path
from .views import *

urlpatterns = [
    path ( 'signup/', sign_up, name='signup' ),
    path ( 'signin/', sign_in, name='signin' ),
    path ( 'signout/', sign_out, name='signout' ),
    path ( '', home, name='home' )
]