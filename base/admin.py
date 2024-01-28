from django.contrib import admin
from .models import Invoices, Invoice_details
# Register your models here.
admin.site.register(Invoices)
admin.site.register(Invoice_details)