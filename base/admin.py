from django.contrib import admin
from .models import Invoices, Invoice_details
# Register your models here.

class InvoicesRef(admin.ModelAdmin):
    list_display = ['id','name', 'date']

class InvoicesDetailsRef(admin.ModelAdmin):
    list_display = ['id','invoice']
admin.site.register(Invoices, InvoicesRef)
admin.site.register(Invoice_details, InvoicesDetailsRef)