from django.contrib import admin
from apps.models import Category, Sub_Category, Product, Contact, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)