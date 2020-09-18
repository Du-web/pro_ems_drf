from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


class UserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        pass
