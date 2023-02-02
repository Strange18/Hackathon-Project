from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('question/<int:id>',question_view,name='question'),
    path('discussion/',discussion,name='discussion'),
]