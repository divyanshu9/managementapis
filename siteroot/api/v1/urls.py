from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from auth1.api.v1 import urls as auth_urls
from survey.api.v1 import urls as survey_urls
from content.api.v1 import urls as content_urls
from project.api.v1 import urls as project_urls

urlpatterns = [
    url(r'auth/', include(auth_urls)),
    url(r'survey/', include(survey_urls)),
    url(r'content/', include(content_urls)),
    url(r'project/', include(project_urls)),
]
