from django.urls import path

from survey.api.v1 import views

urlpatterns = [
    path(r'list_survey/', views.SurveyListAPIView.as_view()),
    path(r'survey_response/', views.SurveyResponseListAPIView.as_view()),
    path(r'product/', views.ProductListAPIView.as_view()),
    path(r'product_category/', views.ProductCatListAPIView.as_view()),
    path(r'<int:id>/', views.SurveyRetrieveAPIView.as_view()),
    path(r'', views.SurveyResponseCreateAPIView.as_view()),
]
