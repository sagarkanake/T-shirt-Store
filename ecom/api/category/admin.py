from re import search
from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_display_links = ('name', 'description', 'created_at')
    list_filter = ('name', 'description', 'created_at')
    search_fields = ('name', 'description', 'created_at')

admin.site.register(Category, CategoryAdmin)