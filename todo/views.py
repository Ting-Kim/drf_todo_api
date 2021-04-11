from .models import Todo, Comment
from .serializers import TodoSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status


class TodoViewSet(viewsets.ModelViewSet):
    """
    할일 리스트 보기, 생성, 디테일 보기, 수정, 삭제 기능을 포함한
    ViewSet 정의
    """
    queryset = Todo.objects.all().order_by('created_at')
    serializer_class = TodoSerializer

    # 요구명세서에 없으므로 PUT Method 차단
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.method == 'PUT':
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_list(request, todo_id):
    """
    댓글 리스트 보기 및 생성
    """
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
    """
    댓글 수정 및 삭제
    """
    comment = Comment.objects.get(id=comment_id)
    request.data['todo'] = todo_id
    if request.method == 'PATCH':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
