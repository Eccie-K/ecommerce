from django.contrib import admin
from .models import Product, Category, tags

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')




admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(tags)