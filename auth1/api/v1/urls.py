from django.urls import path
from django.conf.urls import url

from auth1.api.v1 import views

urlpatterns = [
    path(r'login/', views.Login.as_view()),
    path(r'register/', views.Register.as_view()),
    path(r'change_password/', views.ChangePassword.as_view()),
    path(r'user_role/', views.UserRolesListAPIView.as_view()),
    path(r'user_detail/<int:user__id>/', views.UserRetrieveUpdateAPIView.as_view()),
    path(r'user_detail/', views.UserDetailListAPIView.as_view()),
]
