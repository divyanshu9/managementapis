from django.contrib import admin
from .models import Content, ContentMeta, Comment, PostCategory
# Register your models here.
admin.site.register(Content)
admin.site.register(ContentMeta)
admin.site.register(Comment)
admin.site.register(PostCategory)