from django.db import models
from common.mixins import TrackableMixin
from auth1.models import UserDetail


class Survey(TrackableMixin):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)


class ProductCategory(TrackableMixin):
    name = models.CharField(max_length=250)


class Product(TrackableMixin):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='product_category')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=250)

    @property
    def category_name(self):
        return self.category.name


class SurveyResponse(TrackableMixin):
    submit_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='survey_responses')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='survey_responses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='survey_responses')
    question = models.CharField(max_length=250)
    response = models.CharField(max_length=250)

    @property
    def submit_user_name(self):
        return self.submit_user.user.first_name

    @property
    def product_name(self):
        return self.product.name

    @property
    def category_name(self):
        return self.product.category.name
