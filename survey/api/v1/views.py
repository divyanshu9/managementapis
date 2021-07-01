from rest_framework import status, generics
from survey.models import Survey
from .serializers import SurveySerializer


class SurveyListAPIView(generics.ListAPIView):
    """
    Survey List Api
    """
    serializer_class = SurveySerializer
    queryset = Survey.objects.all().order_by("-id")