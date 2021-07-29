from django.urls import path

from project.api.v1 import views

urlpatterns = [
    path(r'<int:id>/', views.CaseRetrieveUpdateAPIView.as_view()),
    path(r'', views.CaseListCreateAPIView.as_view()),
    path(r'quote/<int:id>/', views.QuoteRetrieveUpdateAPIView.as_view()),
    path(r'quote/', views.QuoteListCreatSeAPIView.as_view()),
    path(r'invoice/<int:id>/', views.InvoiceRetrieveUpdateAPIView.as_view()),
    path(r'invoice/', views.InvoiceListCreateAPIView.as_view()),
    path(r'message/<int:id>/', views.MessageRetrieveUpdateAPIView.as_view()),
    path(r'message/', views.MessageListCreateAPIView.as_view()),
]
