from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo, Comment


class ListTodos(APIView):
    def get(self, request, format=None):
        # todos = Todo.objects.all()
        # serializer = TodoSerializer(todos)
        # return Response(serializer.data)
        return Response(Todo.objects.all())

    def post():
        pass
