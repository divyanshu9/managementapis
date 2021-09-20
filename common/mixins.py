from django.db import models
from rest_framework.response import Response
from rest_framework import status


class TrackableMixin(models.Model):
    """
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    #api_key = models.CharField(max_length=250, blank=True)

    class Meta:
        abstract = True


class APIKEYMixin:

    def create(self, request, *args, **kwargs):
        data = request.data
        data['api_key'] = request.META['HTTP_AUTHORIZATION']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(api_key=request.META['HTTP_AUTHORIZATION'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)