from django.contrib import admin
from sales.models import Sale

# Register your models here.


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer_name', 'payment_method','quantity_ordered','discount']
    search_fields = ['customer_name', 'payment_method']
    extra = 0


