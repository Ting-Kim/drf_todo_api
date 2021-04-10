from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import TodoSerializer, CommentSerializer
from .models import Todo, Comment


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('created_at')
    serializer_class = TodoSerializer


@api_view(['GET', 'POST'])
def comment_list(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'GET':
        comments = Comment.objects.filter(todo=todo)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        contents = request.data['contents']
        request.data['todo'] = todo_id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
def comment_detail(request, todo_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'PATCH':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response("OK")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
