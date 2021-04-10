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


# class TodoSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=30)
#     description = serializers.CharField()
#     is_completed = serializers.BooleanField(default=False)
#     created_at = serializers.DateField()
#     updated_at = serializers.DateField()
#     # title = serializers.CharField(max_length=30, null=False)
#     # description = serializers.TextField(null=False)
#     # is_completed = serializers.BooleanField(default=False)
#     # created_at = serializers.DateField(auto_now_add=True)
#     # updated_at = serializers.DateField(auto_now=True)

#     def create(self, validated_data):
#         return Todo.objects.create(**validated_data)
