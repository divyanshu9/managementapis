from rest_framework import serializers
from content.models import Content, ContentMeta, PostCategory, Comment


class ContentMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentMeta
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class CommentListSerializer(serializers.ModelSerializer):
    parent = CommentCreateSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    content_comment = CommentListSerializer(read_only=True, many=True)
    content_meta = ContentMetaSerializer(read_only=True, many=True)

    class Meta:
        model = Content
        fields = "__all__"


class PostCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = "__all__"


