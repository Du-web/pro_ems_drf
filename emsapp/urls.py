from django.urls import path

from emsapp import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view()),
]