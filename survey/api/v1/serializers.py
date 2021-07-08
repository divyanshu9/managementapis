from rest_framework import serializers
from survey.models import Survey, SurveyResponse, Product


class SurveyResponseSerializer(serializers.ModelSerializer):
    submit_user_name = serializers.ReadOnlyField()

    class Meta:
        model = SurveyResponse
        fields = "__all__"
        extra_kwargs = {'submit_user': {'required': False}}


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
