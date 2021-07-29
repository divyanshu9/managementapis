from django_filters import rest_framework as filters

from project.models import Case


class CaseFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    title = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter()
    product = filters.CharFilter()
    category = filters.CharFilter()
    client_user = filters.NumberFilter()
    case_manager_user = filters.NumberFilter()

    class Meta:
        model = Case
        fields = ['title', 'created_at', 'status', 'product', 'category']
