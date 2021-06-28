from django_filters import rest_framework as filters


# class ApplicationFilter(filters.FilterSet):
#     created = filters.DateFromToRangeFilter()
#     loan_type = filters.MultipleChoiceFilter(choices=Application.LoanType.choices)
#     personnel_number = filters.CharFilter(field_name='personnel_number', lookup_expr='iexact')
#     application_status = filters.CharFilter(field_name='general__loan_application_status')
#
#     class Meta:
#         model = Application
#         fields = ['designation', 'personnel_number', 'loan_type', 'created', 'application_status']