from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Invoices,Invoice_details
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework import status
from rest_framework.response import Response


class InvoicedetailSerializer(ModelSerializer):
    invoice = PrimaryKeyRelatedField(queryset=Invoices.objects.all())  # to avoid circular dependencies 

    class Meta:
        model = Invoice_details
        fields = ['invoice', 'description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(ModelSerializer):
    items = InvoicedetailSerializer(many=True, read_only=True)  # Nested serializer (read-only)
#read_only = 
    class Meta:
        model = Invoices
        fields = '__all__'
    def create(self, validated_data):
        invoice_details_data = validated_data.pop('items', [])
        invoice = Invoices.objects.create(**validated_data)

        # Create associated invoice details
        for invoice_detail_data in invoice_details_data:
            Invoice_details.objects.create(invoice=invoice, **invoice_detail_data)

        return invoice
    

