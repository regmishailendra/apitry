from django.conf.urls import url

from auth.api.views import RegisterApiView, LoginApiView

urlpatterns=[
    url('register',RegisterApiView.as_view()),
    url('login',LoginApiView.as_view()),
]