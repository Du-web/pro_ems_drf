from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from emsapp.serializer import UserModelSerializer
from utils.response import APIResponse


class UserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        user_data = request.data
        print(user_data)
        ser = UserModelSerializer(data=user_data)
        ser.is_valid(raise_exception=True)
        user_obj = ser.save()
        return APIResponse(200, True, results=UserModelSerializer(user_obj).data)
