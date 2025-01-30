from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ["category", "is_active"]
    list_display = ["title", "price", "is_active", "is_deleted"]
    list_editable = ["is_active", "price"]


admin.site.register(models.product, ProductAdmin)
admin.site.register(models.productCategory)
admin.site.register(models.Product_Tags)
admin.site.register(models.product_Brands)
admin.site.register(models.ProductVisitCount)