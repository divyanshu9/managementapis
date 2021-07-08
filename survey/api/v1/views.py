from rest_framework import status, generics
from survey.models import Survey, Product, SurveyResponse
from .serializers import SurveySerializer, ProductSerializer, SurveyResponseSerializer
from .filters import SurveyResponseFilter


class SurveyListAPIView(generics.ListAPIView):
    """
    Survey List Api
    """
    serializer_class = SurveySerializer
    filter_class = SurveyResponseFilter
    queryset = SurveyResponse.objects.all().order_by("-id")


class SurveyResponseListAPIView(generics.ListAPIView):
    """
    Survey Response List Api
    """
    serializer_class = SurveyResponseSerializer
    queryset = Survey.objects.all().order_by("-id")


class ProductListAPIView(generics.ListAPIView):
    """
    Product List Api
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-id")