from rest_framework.generics import CreateAPIView, ListAPIView

from comments.api.serializer import CommentsListSerializer, CommentCreateSerializer
from comments.models import CommentsModel


class CommentsListAPIView(ListAPIView):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentsListSerializer




class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
