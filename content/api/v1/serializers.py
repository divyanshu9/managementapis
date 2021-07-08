from rest_framework import serializers
from content.models import Content, ContentMeta, Comment


class ContentMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentMeta
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {'parent': {'required': False}}


class CommentListSerializer(serializers.ModelSerializer):
    parent = CommentCreateSerializer(read_only=True)
    author_name = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField()
    content_comment = CommentListSerializer(read_only=True, many=True)
    content_meta = ContentMetaSerializer(read_only=True, many=True)

    class Meta:
        model = Content
        fields = "__all__"


