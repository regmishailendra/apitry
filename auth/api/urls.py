from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from auth.api.views import RegisterApiView, LoginApiView

urlpatterns=[
    url('register',RegisterApiView.as_view()),
    url('login',LoginApiView.as_view()),
    url('token',obtain_jwt_token),
]