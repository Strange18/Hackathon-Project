from django.urls import path
from .views import *

urlpatterns = [
    path('idea_view/', view_items, name='idea_view'),
    path('idea_add/', add_item, name='idea_add'),
    path('idea_update/<int:pk>', update_item, name='idea_update'),
    path('idea_delete/<int:pk>', delete_item, name='idea_delete'),

]
