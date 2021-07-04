from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from content.models import Content, ContentMeta, PostCategory, Comment
from .serializers import ContentSerializer, ContentMetaSerializer, PostCategorySerializer, CommentSerializer
# Create your views here.


class ContentListCreateAPIView(generics.ListCreateAPIView):
    """
    Content Create and List Api
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all().order_by("-id")


class ContentMetaListCreateAPIView(generics.ListCreateAPIView):
    """
    Content Meta Create and List Api
    """
    serializer_class = ContentMetaSerializer
    queryset = ContentMeta.objects.all().order_by("-id")


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    Comment Create and List Api
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by("-id")


class PostCategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    PostCategory Create and List Api
    """
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all().order_by("-id")


class ContentRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Content Retrieve Update and Destroy Api
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all().order_by("-id")


class ContentMetaRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Content Meta Retrieve Update and Destroy Api
    """
    serializer_class = ContentMetaSerializer
    queryset = ContentMeta.objects.all().order_by("-id")


class CommentRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Comment Retrieve Update and Destroy Api
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by("-id")


class PostCategoryRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    PostCategory Retrieve Update and Destroy Api
    """
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all().order_by("-id")
