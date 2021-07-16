from django_filters import rest_framework as filters

from survey.models import SurveyResponse, Product


class SurveyResponseFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()
    submit_user = filters.NumberFilter()
    survey = filters.NumberFilter()
    product = filters.NumberFilter()
    category = filters.CharFilter()

    class Meta:
        model = SurveyResponse
        fields = ['submit_user', 'created', 'survey', 'product', 'category']


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = ['category']
