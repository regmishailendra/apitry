from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from story.models import StoryModel


class CommentsModel(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    story = models.ForeignKey(StoryModel,related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content