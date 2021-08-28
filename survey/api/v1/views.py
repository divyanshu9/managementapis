from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from survey.models import Survey, Product, SurveyResponse, ProductCategory
from .serializers import SurveySerializer, ProductSerializer, SurveyResponseSerializer, \
    SurveyResponseCreateSerializer, SurveyResponseReadSerializer, ProductCatSerializer
from .filters import SurveyResponseFilter, ProductFilter


class SurveyListAPIView(generics.ListAPIView):
    """
    Survey List Api
    """
    serializer_class = SurveySerializer
    queryset = Survey.objects.all().order_by("-id")


class SurveyRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Survey Retrieve Api
    """
    serializer_class = SurveySerializer
    lookup_field = "id"
    queryset = Survey.objects.all().order_by("-id")


class SurveyResponseListAPIView(generics.ListAPIView):
    """
    Survey Response List Api
    """
    serializer_class = SurveyResponseReadSerializer
    filter_class = SurveyResponseFilter
    queryset = SurveyResponse.objects.all().order_by("-id")


class SurveyResponseCreateAPIView(generics.CreateAPIView):
    serializer_class = SurveyResponseCreateSerializer
    queryset = SurveyResponse.objects.all().order_by("-id")


class ProductListAPIView(generics.ListAPIView):
    """
    Product List Api
    """
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    queryset = Product.objects.all().order_by("-id")


class ProductCatListAPIView(generics.ListAPIView):
    """
    Product List Api
    """
    serializer_class = ProductCatSerializer
    queryset = ProductCategory.objects.all().order_by("-id")