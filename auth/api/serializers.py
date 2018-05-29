import requests
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.utils import json

from comments.api import serializer


class UserCreateSerializer(ModelSerializer):
    token=serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password','token']
        extra_kwargs = {"password": {
            "write_only": True
        }}

    def create(self, validated_data):

        username= validated_data['username']
        email=validated_data['email']
        password=validated_data['password']
        user=User(username=username,email=email)
        user.set_password(password)
        user.save()
        validated_data['token']=getToken(username,password)
        return validated_data


def getToken(username,password):
    post_data = [('username', username), ('password', password)]
    result = requests.post('http://127.0.0.1:8000/auth/token', data=post_data)
    content = json.loads(result.text)
    return content['token']


class UserLoginSerializer(ModelSerializer):
    token=serializers.CharField(allow_blank=True,read_only=True)
    username=serializers.CharField(allow_blank=True,required=False)
    email=serializers.EmailField(label="Email Address",required=False)



    class Meta:
        model = User
        fields = ['username','token','email','password']
        extra_kwargs = {"password": {
            "write_only": True
        }}




    def validate(self, attrs):
          email= attrs.get("email",None)
          username=attrs.get("username",None)
          password=attrs.get("password")
          if not email and not username:
              raise ValidationError("Email or username is required")
          user=User.objects.filter(
              Q(email=email)|Q(username=username)).distinct()
          if user.exists() and user.count()==1:
              user_obj=user.first()

          else:
              raise ValidationError("This username/email is not valid.")

          if user_obj:
              if not user_obj.check_password(password):
                  raise ValidationError("Incorrect credentials please try again")

          attrs["token"]=getToken(username,password)
          return attrs