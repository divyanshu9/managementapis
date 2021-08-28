from django.contrib import admin
from .models import Survey, SurveyResponse, ProductCategory, Product, Response

admin.site.register(Survey)
admin.site.register(SurveyResponse)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Response)
