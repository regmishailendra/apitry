from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from comments.api.serializer import CommentsListSerializer
from story.models import StoryModel


class StoryCreateSerializer(ModelSerializer):

    class Meta:
        model = StoryModel
        fields = ['title', 'content', 'full_detail']


class StoryListSerializer(ModelSerializer):
    user = SerializerMethodField()
    comments=CommentsListSerializer(many=True,read_only=True)

    class Meta:
        model = StoryModel
        fields = ['pk', 'title', 'content', 'updated', 'user','comments']

    def get_user(self, obj):
        return obj.user.get_full_name()


class StoryDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    comments=CommentsListSerializer(many=True,read_only=True)


    class Meta:
        model = StoryModel
        fields = ['pk', 'title', 'content', 'created', 'updated', 'user', 'full_detail','comments']

    def get_user(self, obj):
        return obj.user.get_full_name()
