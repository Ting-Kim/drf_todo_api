from django.urls import path
from .views import ListTodos

app_name = 'todo'

urlpatterns = [
    path('', ListTodos.as_view(), name='list_todo'),
]
