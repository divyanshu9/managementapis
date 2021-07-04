from django.db import models
from common.mixins import TrackableMixin
from auth1.models import UserDetail
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Content(TrackableMixin):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    url = models.URLField()
    title = models.CharField(max_length=250)
    body = models.TextField()


class PostCategory(TrackableMixin):

    class Category(models.TextChoices):
        CAT_1 = 'C1', _('Category one')
        CAT_2 = 'C2', _('Category two')

    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    category = models.CharField(
        _('category'), max_length=2, choices=Category.choices
    )


class ContentMeta(TrackableMixin):

    post = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name="content_meta")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="content_meta")
    meta_key = models.CharField(max_length=250)
    meta_content = models.CharField(max_length=250)


class Comment(TrackableMixin):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_comment')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    status_comment = models.CharField(max_length=250)
    body = models.TextField()