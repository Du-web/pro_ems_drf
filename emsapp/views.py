from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from emsapp.serializer import UserModelSerializer, EmployeeModelSerializer
from utils.response import APIResponse
from emsapp.models import User, Employee


class UserRegister(APIView):

    def post(self, request, *args, **kwargs):
        user_data = request.data
        print(user_data)
        ser = UserModelSerializer(data=user_data, context={'request': request})
        ser.is_valid(raise_exception=True)
        user_obj = ser.save()
        return APIResponse(200, True, results=UserModelSerializer(user_obj).data)


class UserLogin(APIView):

    def post(self, request, *args, **kwargs):
        permission_classes = []
        authentication_classes = []
        print(request.data)
        name = request.data.get("username")
        pwd = request.data.get("password")
        user_obj = User.objects.filter(username=name, password=pwd).first()
        if user_obj:
            data = UserModelSerializer(user_obj).data
            return APIResponse(200, True, results=data)
        return APIResponse(400, False)


class EmployeeGenericAPIView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            response = self.retrieve(request, *args, **kwargs)
            return APIResponse(200, True, results=response.data)
        response = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=response.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        emp_obj = self.create(request, *args, **kwargs)
        return APIResponse(200, True, results=emp_obj.data)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        emp_list = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=emp_list.data)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        self.partial_update(request, *args, **kwargs)
        return APIResponse(200, True)