from django.db import models


class Todo(models.Model):
    """ Todo Model Definition """

    title = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Comment(models.Model):
    """ Comment Model Definition """

    contents = models.CharField(max_length=100, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
