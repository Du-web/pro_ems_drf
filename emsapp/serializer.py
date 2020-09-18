from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions

from emsapp.models import User, Employee


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'real_name', 'password', 'gender')
        extra_kwargs = {
            'username': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '用户名必填',
                    'min_length': '用户名的长度不够'
                },
            },
            'password': {
                'write_only': True,
            },
            'real_name': {
                'write_only': True,
            }
        }

    def validate_username(self, attrs):
        user = User.objects.filter(username=attrs).first()
        if user:
            raise exceptions.ValidationError("用户名已存在")
        return attrs

    def validate_password(self, attrs):
        request = self.context.get('request')
        re_pwd = request.data.get('re_pwd')
        if re_pwd == attrs:
            if len(attrs) < 6:
                raise exceptions.ValidationError('密码长度不能小于6')
            return attrs
        else:
            raise exceptions.ValidationError('两次密码不一致')


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'emp_name', 'img', 'salary', 'age')

        extra_kwargs = {
            "emp_name": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }