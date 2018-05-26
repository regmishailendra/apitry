from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from story.api.serializers import StoryListSerializer, StoryDetailSerializer, StoryCreateSerializer
from story.models import StoryModel


class StoryCreateAPIView(CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = StoryCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryListView(ListAPIView):
    serializer_class = StoryListSerializer
    queryset = StoryModel.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return StoryModel.objects.filter(
                Q(user__first_name__icontains=query) |
                Q(title__icontains=query) |
                Q(content__icontains=query))

        else:
            return StoryModel.objects.all()


class StoryDetailAPIView(RetrieveAPIView):
    serializer_class = StoryDetailSerializer
    queryset = StoryModel.objects.all()
