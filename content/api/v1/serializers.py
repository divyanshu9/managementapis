from rest_framework import serializers
from content.models import Content, ContentMeta, PostCategory, Comment


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = "__all__"


class ContentMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentMeta
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class PostCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = "__all__"


