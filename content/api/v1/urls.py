from django.urls import path

from content.api.v1 import views

urlpatterns = [
    path(r'<int:id>/', views.ContentRetrieveUpdateAPIView.as_view()),
    path(r'', views.ContentListCreateAPIView.as_view()),
    path(r'meta/<int:id>/', views.ContentMetaRetrieveUpdateAPIView.as_view()),
    path(r'meta/', views.ContentMetaListCreateAPIView.as_view()),
    path(r'comment/<int:id>/', views.CommentRetrieveUpdateAPIView.as_view()),
    path(r'list_comment/', views.CommentListAPIView.as_view()),
    path(r'comment/', views.CommentCreateAPIView.as_view()),
]
