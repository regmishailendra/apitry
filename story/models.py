from django.contrib.auth.models import User
from django.db import models


class StoryModel(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    full_detail = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
