from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.api.serializers import UserCreateSerializer, UserLoginSerializer


class RegisterApiView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]




class LoginApiView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self,request):
        data=request.data
        serializer=UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return Response(new_data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





