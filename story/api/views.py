from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from story.api.serializers import StoryListSerializer, StoryDetailSerializer, StoryCreateSerializer
from story.models import StoryModel


class StoryCreateAPIView(CreateAPIView):
    serializer_class = StoryCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





class StoryListView(ListAPIView):
    serializer_class = StoryListSerializer
    queryset = StoryModel.objects.all()









class StoryDetailAPIView(RetrieveAPIView):
    serializer_class = StoryDetailSerializer
    queryset = StoryModel.objects.all()
