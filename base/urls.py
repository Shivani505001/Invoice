# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.front),  
    path('invoices/', views.all_invoices,name='all-invoices'),
    path('invoices/<int:invoice_id>/', views.details, name='invoice-detail'),
]
