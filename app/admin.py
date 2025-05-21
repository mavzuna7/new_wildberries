from django.contrib import admin
from .models import Product, Category, Brand
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand) 


