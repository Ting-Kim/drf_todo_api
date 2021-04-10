from rest_framework import serializers
from .models import Todo, Comment


class TodoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    todo = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Todo.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'contents', 'created_at', 'updated_at', 'todo']
