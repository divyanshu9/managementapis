from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from django_filters import rest_framework as filters

from content.models import Content, ContentMeta, Comment
from common.mixins import APIKEYMixin
from .serializers import ContentSerializer, ContentMetaSerializer,\
    CommentCreateSerializer, CommentListSerializer
from .filters import ContentFilter
# Create your views here.


class ContentListCreateAPIView(APIKEYMixin, generics.ListCreateAPIView):
    """
    Content Create and List Api
    """
    serializer_class = ContentSerializer
    filter_class = ContentFilter
    ordering_fields = ('id', 'category', 'title', 'url', ('author', 'author__first_name'), 'created_at')
    ordering = ['-id']
    queryset = Content.objects.all()


class ContentMetaListCreateAPIView(APIKEYMixin, generics.ListCreateAPIView):
    """
    Content Meta Create and List Api
    """
    serializer_class = ContentMetaSerializer
    queryset = ContentMeta.objects.all().order_by("-id")


class CommentCreateAPIView(APIKEYMixin, generics.CreateAPIView):
    """
    Comment Create and List Api
    """
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all().order_by("-id")


class CommentListAPIView(APIKEYMixin, generics.ListAPIView):
    """
    Comment List Api
    """
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all().order_by("-id")


class ContentRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Content Retrieve Update and Destroy Api
    """
    serializer_class = ContentSerializer
    lookup_field = "id"
    queryset = Content.objects.all().order_by("-id")


class ContentMetaRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Content Meta Retrieve Update and Destroy Api
    """
    serializer_class = ContentMetaSerializer
    lookup_field = "id"
    queryset = ContentMeta.objects.all().order_by("-id")


class CommentRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Comment Retrieve Update and Destroy Api
    """
    serializer_class = CommentCreateSerializer
    lookup_field = "id"
    queryset = Comment.objects.all().order_by("-id")
