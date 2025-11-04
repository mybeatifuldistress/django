from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created_at', 'updated_at', 'availability']
    list_filter = ['category', 'availability', 'created_at', 'updated_at']
    list_editable = ['price', 'availability']
    prepopulated_fields = {'slug': ('name',)}
