from rest_framework import serializers
from project.models import Case, Quote, Message, Invoice, Attachment


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = "__all__"


class CaseSerializer(serializers.ModelSerializer):
    client_user_name = serializers.ReadOnlyField()
    case_manager_user_name = serializers.ReadOnlyField()

    class Meta:
        model = Case
        fields = "__all__"
        extra_kwargs = {'client_user': {'required': False}}


class QuoteSerializer(serializers.ModelSerializer):
    submit_user_name = serializers.ReadOnlyField()
    recipient_user_name = serializers.ReadOnlyField()
    attachment = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Quote
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    submit_user_name = serializers.ReadOnlyField()
    attachment = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    submit_user_name = serializers.ReadOnlyField()
    recipient_user_name = serializers.ReadOnlyField()
    attachment = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = "__all__"


