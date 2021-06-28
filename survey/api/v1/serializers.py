from rest_framework import serializers
from survey.models import Survey, SurveyResponse


class SurveyResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyResponse
        fields = "__all__"
        extra_kwargs = {'submit_user': {'required': False}}


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = "__all__"


