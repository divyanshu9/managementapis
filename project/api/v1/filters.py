from django_filters import rest_framework as filters

from project.models import Case, Quote, Invoice, Message, Attachment


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


class QuoteFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    comment = filters.CharFilter(lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter()
    price = filters.NumberFilter()
    recipient_user = filters.NumberFilter()
    submit_user = filters.NumberFilter()
    case = filters.NumberFilter()

    class Meta:
        model = Quote
        fields = ['case', 'comment', 'title', 'created_at', 'status', 'price', 'recipient_user', 'submit_user']


class InvoiceFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    comment = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter()
    price = filters.NumberFilter()
    recipient_user = filters.NumberFilter()
    submit_user = filters.NumberFilter()
    case = filters.NumberFilter()

    class Meta:
        model = Invoice
        fields = ['case', 'comment', 'created_at', 'status', 'price', 'recipient_user', 'submit_user']


class MessageFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    submit_user = filters.NumberFilter()
    case = filters.NumberFilter()

    class Meta:
        model = Message
        fields = ['case', 'created_at', 'submit_user']


class AttachmentFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    message = filters.NumberFilter()
    quote = filters.NumberFilter()
    invoice = filters.NumberFilter()
    url = filters.CharFilter()

    class Meta:
        model = Attachment
        fields = ['message', 'created_at', 'quote', 'invoice', 'url']
