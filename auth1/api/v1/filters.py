from django_filters import rest_framework as filters

from auth1.models import UserDetail


class UserDetailFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    location = filters.CharFilter()
    status = filters.NumberFilter()
    user_role = filters.NumberFilter()

    class Meta:
        model = UserDetail
        fields = ['created_at', 'location', 'status', 'user_role']
