from django.urls import path
from django.conf.urls import url

from auth1.api.v1 import views

urlpatterns = [
    path(r'login/', views.Login.as_view()),
    path(r'register/', views.Register.as_view()),
    path(r'change_password/', views.ChangePassword.as_view()),
    url(r"^activate/b'(?P<uidb64>[0-9A-Za-z_\-]+)'/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        views.activate, name='activate'),
]
