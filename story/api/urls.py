from django.conf.urls import url

from story.api.views import StoryListView, StoryDetailAPIView, StoryCreateAPIView

urlpatterns=[

    url(r'^$', StoryListView.as_view()),

    url('(?P<pk>\d+)/detail',StoryDetailAPIView.as_view()),

    url(r'^create',StoryCreateAPIView.as_view()),
]