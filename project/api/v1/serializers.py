from rest_framework import serializers
from project.models import Case, Quote, Message, Invoice, Attachment


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = "__all__"
        extra_kwargs = {'client_user': {'required': False}}


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = "__all__"

