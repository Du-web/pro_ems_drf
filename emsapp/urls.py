from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from emsapp import views

urlpatterns = [
    # 带用户名和密码参数生成token
    url(r'^login_out/', obtain_jwt_token),
    path('register/', views.UserRegister.as_view()),
    path('register/<str:id>/', views.UserRegister.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('login/<str:id>/', views.UserLogin.as_view()),
    path('emp/', views.EmployeeGenericAPIView.as_view()),
    path('emp/<str:id>/', views.EmployeeGenericAPIView.as_view()),
]
