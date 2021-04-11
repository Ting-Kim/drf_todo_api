from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todos/', include('todo.urls', namespace='todo')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
