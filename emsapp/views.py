from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from emsapp.serializer import UserModelSerializer
from utils.response import APIResponse
from emsapp.models import User, Employee


class UserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        user_data = request.data
        print(user_data)
        ser = UserModelSerializer(data=user_data, context={'request': request})
        ser.is_valid(raise_exception=True)
        user_obj = ser.save()
        return APIResponse(200, True, results=UserModelSerializer(user_obj).data)

    def get(self, request, *args, **kwargs):

        name = request.query_params.get("username")
        pwd = request.query_params.get("password")
        user_obj = User.objects.filter(username=name, password=pwd).first()
        if user_obj:
            data = UserModelSerializer(user_obj).data
            return APIResponse(200, True, results=data)
        return APIResponse(400, False)
