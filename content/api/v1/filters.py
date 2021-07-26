from django_filters import rest_framework as filters

from content.models import Content


class ContentFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()
    url = filters.CharFilter()
    title = filters.CharFilter(lookup_expr='icontains')
    body = filters.CharFilter()
    category = filters.CharFilter()
    type = filters.CharFilter()

    class Meta:
        model = Content
        fields = ['url', 'created', 'title', 'body', 'category', 'type']
