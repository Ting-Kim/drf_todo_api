from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'todo'

urlpatterns = [
    path('<int:todo_id>/comments/', views.comment_list, name='comment_list'),
    path('<int:todo_id>/comments/<int:cooment_id>/',
         views.comment_detail, name='comment_detail'),
]
