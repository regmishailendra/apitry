from django.conf.urls import url

from comments.api.views import CommentsListAPIView, CommentCreateAPIView

urlpatterns=[
    url('list',CommentsListAPIView.as_view()),
    url('create',CommentCreateAPIView.as_view()),


]



