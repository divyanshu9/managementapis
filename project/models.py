from django.db import models
from common.mixins import TrackableMixin
from auth1.models import UserDetail
from survey.models import ProductCategory, Product


class Case(TrackableMixin):
    client_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='case')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    case_manager_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='case_manager')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=250)


class Quote(TrackableMixin):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='quote')
    recipient_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='quote_user')
    submit_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='quote_sumbit_user')
    price = models.IntegerField()
    status = models.CharField(max_length=250)
    comment = models.CharField(max_length=250)


class Invoice(TrackableMixin):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='case_invoice')
    recipient_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='invoice')
    submit_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='invoice_submit_user')
    price = models.IntegerField()
    status = models.CharField(max_length=250)
    comment = models.CharField(max_length=250)


class Message(TrackableMixin):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='message')
    submit_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='message')
    message = models.TextField()


class Attachment(TrackableMixin):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachment')
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='attachment')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='attachment')
    url = models.URLField()