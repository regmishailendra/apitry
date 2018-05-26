from django.db.models import Q
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from comments.api.serializer import CommentsListSerializer, CommentCreateSerializer
from comments.models import CommentsModel
from story.models import StoryModel


class CommentsListAPIView(ListAPIView):
    queryset = CommentsModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentsListSerializer



    def get_queryset(self):

        query=self.request.GET.get('q')
        if query:
            print(query)
            queryset=CommentsModel.objects.filter(
                Q(content__icontains=query)  |
                Q(user__first_name__icontains=query)
            )

            return queryset
        else:
            return CommentsModel.objects.all()








class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            story_key = serializer.validated_data['story_id']
            story = StoryModel.objects.filter(pk=story_key).first()

            if (story):
                print('passed to create')
                self.perform_create(serializer)
                return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        if serializer.is_valid():
            story_key = serializer.validated_data['story_id']
            story = StoryModel.objects.filter(pk=story_key).first()
            if story:
                print("serializer is valid")
                serializer.save(user=self.request.user, story=story)
                print("serializer saved")
            else:
                return ValidationError('This story does not exists.')
