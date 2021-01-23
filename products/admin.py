from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'subject',
        'rating',
        'price',
        'year',
        'image',
        'grade',
    )

    ordering = ('grade',)


admin.site.register(Product, ProductAdmin)
