from django.urls import path
from authentications.views import *

app_name = 'authentications'

urlpatterns = [
    # path('', index, name='index'),
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
]



