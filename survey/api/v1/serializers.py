from rest_framework import serializers
from survey.models import Survey, SurveyResponse, Product, Response, ProductCategory
from auth1.models import UserDetail


class UserIDNameSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = UserDetail
        fields = ("id", "name")


class SurveyIDNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ("id", "title")


class ProductIDNameSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ("id", "name", "category_name")


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = "__all__"
        extra_kwargs = {'survey_response': {'required': False}}


class SurveyResponseSerializer(serializers.ModelSerializer):
    submit_user_data = UserIDNameSerializer(read_only=True)
    product_data = ProductIDNameSerializer(read_only=True)
    responses = ResponseSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyResponse
        fields = "__all__"
        extra_kwargs = {'submit_user': {'required': False}}


class SurveyResponseReadSerializer(serializers.ModelSerializer):
    submit_user = UserIDNameSerializer(read_only=True)
    product = ProductIDNameSerializer(read_only=True)
    survey = SurveyIDNameSerializer(read_only=True)
    responses = ResponseSerializer(many=True)

    class Meta:
        model = SurveyResponse
        fields = ('survey', 'submit_user', 'product', 'responses', 'created_at', 'modified_at')


class SurveyResponseCreateSerializer(serializers.ModelSerializer):
    submit_user_data = UserIDNameSerializer(read_only=True)
    product_data = ProductIDNameSerializer(read_only=True)
    responses = ResponseSerializer(many=True)

    class Meta:
        model = SurveyResponse
        fields = "__all__"

    def create(self, validated_data):
        responses = validated_data.pop("responses")
        survey_response = SurveyResponse.objects.create(**validated_data)
        for response in responses:
            Response.objects.create(
                survey_response=survey_response, **response)
        return survey_response


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = "__all__"


class ProductCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = "__all__"
