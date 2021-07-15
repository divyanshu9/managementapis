from django.db import models
from common.mixins import TrackableMixin
from auth1.models import UserDetail
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Content(TrackableMixin):

    class Category(models.TextChoices):
        CAT_1 = 'MW', _('Modern Workplace')
        CAT_2 = 'CP', _('Customer Portal')
        CAT_3 = 'BI', _('BI Report')
        CAT_4 = 'BC', _('Business Consulting')

    class Status(models.TextChoices):
        FEATURED = 'F', _('Featured')
        ORDINARY = 'O', _('Ordinary')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        _('status'), max_length=1, choices=Status.choices
    )
    type = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.TextField()
    category = models.CharField(
        _('category'), max_length=2, choices=Category.choices, null=True, blank=True
    )

    @property
    def author_name(self):
        return self.author.first_name


class ContentMeta(TrackableMixin):

    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="content_meta")
    meta_key = models.CharField(max_length=250)
    meta_content = models.CharField(max_length=250)


class Comment(TrackableMixin):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_comment')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='parent_comment')
    status_comment = models.CharField(max_length=250)
    body = models.TextField()

    @property
    def author_name(self):
        return self.author.first_name
