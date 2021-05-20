from django.urls import path
from .views import *

urlpatterns = [
    path('register-user', RegisterUser.as_view()),
    path('login-user', LoginUser.as_view()),
    path('logout-user', LogoutUser.as_view())
]
