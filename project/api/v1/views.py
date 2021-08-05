from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from django_filters import rest_framework as filters

from project.models import Case, Quote, Invoice, Message, Attachment
from .serializers import CaseSerializer, QuoteSerializer,\
    InvoiceSerializer, MessageSerializer, AttachmentSerializer
from .filters import CaseFilter, QuoteFilter, InvoiceFilter, MessageFilter, AttachmentFilter
# Create your views here.


class CaseListCreateAPIView(generics.ListCreateAPIView):
    """
    Case Create and List Api
    """
    serializer_class = CaseSerializer
    filter_class = CaseFilter
    ordering_fields = ('id', 'category', 'title',
                       ('client', 'client_user__userdetails__first_name'),
                       ('case_manager', 'case_manager_user__userdetails__first_name'), 'created_at')
    ordering = ['-id']
    queryset = Case.objects.all()


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    """
    Quote Create and List Api
    """
    serializer_class = QuoteSerializer
    filter_class = QuoteFilter
    ordering_fields = ('id', 'case', 'price',
                       ('recipient_user', 'recipient_user__userdetails__first_name'),
                       ('submit_user', 'submit_user__userdetails__first_name'), 'created_at')
    ordering = ['-id']
    queryset = Quote.objects.all()


class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    """
    Invoice Create and List Api
    """
    serializer_class = InvoiceSerializer
    filter_class = InvoiceFilter
    ordering_fields = ('id', 'case', 'price',
                       ('recipient_user', 'recipient_user__userdetails__first_name'),
                       ('submit_user', 'submit_user__userdetails__first_name'), 'created_at')
    ordering = ['-id']
    queryset = Invoice.objects.all()


class MessageListCreateAPIView(generics.ListCreateAPIView):
    """
    Message Create and List Api
    """
    serializer_class = MessageSerializer
    filter_class = MessageFilter
    ordering_fields = ('id', 'case',
                       ('submit_user', 'submit_user__first_name'),
                       'created_at')
    ordering = ['-id']
    queryset = Message.objects.all()


class AttachmentListCreateAPIView(generics.ListCreateAPIView):
    """
    Attachment Create and List Api
    """
    serializer_class = AttachmentSerializer
    filter_class = AttachmentFilter
    ordering_fields = ('id', 'message', 'quote', 'url',
                       'created_at')
    ordering = ['-id']
    queryset = Attachment.objects.all()


class CaseRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Case Retrieve Update and Destroy Api
    """
    serializer_class = CaseSerializer
    lookup_field = "id"
    queryset = Case.objects.all().order_by("-id")


class QuoteRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Quote Retrieve Update and Destroy Api
    """
    serializer_class = QuoteSerializer
    lookup_field = "id"
    queryset = Quote.objects.all().order_by("-id")


class InvoiceRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Invoice Retrieve Update and Destroy Api
    """
    serializer_class = InvoiceSerializer
    lookup_field = "id"
    queryset = Invoice.objects.all().order_by("-id")


class MessageRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Message Retrieve Update and Destroy Api
    """
    serializer_class = MessageSerializer
    lookup_field = "id"
    queryset = Message.objects.all().order_by("-id")