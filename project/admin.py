from django.contrib import admin
from .models import Case, Quote, Invoice, Message, Attachment
# Register your models here.
admin.site.register(Case)
admin.site.register(Quote)
admin.site.register(Invoice)
admin.site.register(Message)
admin.site.register(Attachment)