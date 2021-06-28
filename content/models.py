from django.db import models
from common.mixins import TrackableMixin
from auth1.models import UserDetail


# class Survey(TrackableMixin):
#     title = models.CharField(max_length=250)
#     content = models.CharField(max_length=250)
#
#
# class SurveyResponses(TrackableMixin):
#     submit_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='survey_responses')
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='survey_responses')