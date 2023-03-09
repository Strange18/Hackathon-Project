from django.urls import path
from .views import *

urlpatterns = [
    # path('',home,name='home'),
    path('idea/',idea_add,name='idea_add'),
    path('complain/',complain_add,name='complain_add'),
    path('idea_view/',idea_view,name='idea_view'),
    path('complain_view/',complain_view,name='complain_view'),
    # path('suggestion/',suggestion,name='suggestion'),
    path('generate/',generate_txt,name='generate'),
    path('complain/<int:id>',complain_view_each,name='complain_view_each'),
    path('idea/<int:id>',idea_view_each,name='idea_view_each'),
    path('like/<int:id>',complain_like_view,name='complain_like'),
    path('dislike/<int:id>',complain_dislike_view,name='complain_dislike'),
    path('idea_like/<int:id>',idea_like_view,name='idea_like'),
    path('idea_dislike/<int:id>',idea_dislike_view,name='idea_dislike'),   
]

