from csv import list_dialects
from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'transaction_id', 'total_amount')
    list_display_links = ('user', 'transaction_id', 'total_amount')
    list_filter = ('user', 'transaction_id', 'total_amount')
    search_fields = ('user', 'transaction_id', 'total_amount')
    
    

admin.site.register(Order, OrderAdmin)