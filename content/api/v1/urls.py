from django.urls import path

from content.api.v1 import views

urlpatterns = [
    path(r'<int:pk>/', views.ContentRetrieveUpdateAPIView.as_view()),
    path(r'', views.ContentListCreateAPIView.as_view()),
    path(r'meta/<int:pk>/', views.ContentMetaRetrieveUpdateAPIView.as_view()),
    path(r'meta/', views.ContentMetaListCreateAPIView.as_view()),
    path(r'comment/<int:pk>/', views.CommentRetrieveUpdateAPIView.as_view()),
    path(r'list_comment/', views.CommentListAPIView.as_view()),
    path(r'comment/', views.CommentCreateAPIView.as_view()),
]
