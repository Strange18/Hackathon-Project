from django.urls import path
from .views import *

urlpatterns =[
    path('login',login_user,name='login'),
    path('signup',signup,name='signup'),
    path('logout',logout_user,name='logout'),
]