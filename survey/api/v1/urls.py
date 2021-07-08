from django.urls import path

from survey.api.v1 import views

urlpatterns = [
    path(r'list_survey/', views.SurveyListAPIView.as_view()),
    path(r'product/', views.SurveyListAPIView.as_view()),
]
