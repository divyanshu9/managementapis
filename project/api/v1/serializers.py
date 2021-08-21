from rest_framework import serializers
from project.models import Case, Quote, Message, Invoice, Attachment


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = "__all__"


class CaseSerializerShort(serializers.ModelSerializer):
    client_user_name = serializers.ReadOnlyField()
    case_manager_user_name = serializers.ReadOnlyField()

    class Meta:
        model = Case
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    submit_user_name = serializers.ReadOnlyField()
    recipient_user_name = serializers.ReadOnlyField()
    attachment = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Quote
        fields = "__all__"


class QuoteSerializerWithCase(serializers.ModelSerializer):
    submit_user_name = serializers.ReadOnlyField()
    recipient_user_name = serializers.ReadOnlyField()
    attachment = AttachmentSerializer(many=True, read_only=True)
    case = CaseSerializerShort(read_only=True)

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


class InvoiceSerializerWithCase(serializers.ModelSerializer):
    submit_user_name = serializers.ReadOnlyField()
    recipient_user_name = serializers.ReadOnlyField()
    attachment = AttachmentSerializer(many=True, read_only=True)
    case = CaseSerializerShort(read_only=True)

    class Meta:
        model = Invoice
        fields = "__all__"


class CaseSerializer(serializers.ModelSerializer):
    client_user_name = serializers.ReadOnlyField()
    case_manager_user_name = serializers.ReadOnlyField()
    case_invoice = InvoiceSerializer(many=True, read_only=True)
    quote = QuoteSerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = "__all__"
        extra_kwargs = {'client_user': {'required': False}}

