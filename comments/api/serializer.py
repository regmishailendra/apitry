from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from comments.models import CommentsModel


class CommentsListSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = CommentsModel
        fields = ['content', 'updated', 'created', 'story', 'user']

    def get_user(self, obj):
        return obj.user.get_full_name()



class CommentCreateSerializer(ModelSerializer):

    story_id= serializers.IntegerField()

    class Meta:
        model = CommentsModel
        fields = ['content', 'story_id']

















