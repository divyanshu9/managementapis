from django.urls import path

from projectmanagement.project.api.v1 import views

urlpatterns = [
    path(r'login/', views.Login.as_view()),
    path(r'register/', views.Register.as_view()),
]
