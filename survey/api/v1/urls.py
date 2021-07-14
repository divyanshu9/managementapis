from django.urls import path

from survey.api.v1 import views

urlpatterns = [
    path(r'list_survey/', views.SurveyListAPIView.as_view()),
    path(r'survey_response/', views.SurveyResponseListAPIView.as_view()),
    path(r'product/', views.SurveyListAPIView.as_view()),
    path(r'', views.SurveyResponseCreateAPIView.as_view()),
]
