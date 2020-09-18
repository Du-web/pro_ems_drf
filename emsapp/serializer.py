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