from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Invoice_details,Invoices
from rest_framework.views import APIView
from .serializer import InvoiceSerializer,InvoicedetailSerializer
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET','POST','DELETE'])

def all_invoices(request):
    invoices=Invoices.objects.all()  
    if request.method=='GET':
        
        serializer=InvoiceSerializer(invoices,many=True)
        return Response(serializer.data)
        
    elif request.method=='POST':
        serializer=InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method=='DELETE':
    #     invoices.delete() #to delete all invoices 
    #     return Response("DONE")
    
    elif request.method == 'DELETE':
        # Retrieve the specific invoice based on the 'pk' parameter
        invoice_id = request.data.get('pk')
        if not invoice_id:
            return Response("Missing 'pk' parameter", status=status.HTTP_400_BAD_REQUEST) 
        try:
            
            invoice = Invoices.objects.get(pk=invoice_id)
            invoice.delete()
            return Response("Invoice deleted", status=status.HTTP_200_OK)
           
        except Invoices.DoesNotExist:
            return Response("Invoice not found", status=status.HTTP_404_NOT_FOUND)
        
    
@api_view(['GET','PUT','DELETE','POST'])

def details(request,invoice_id):
    invoices_detail = {}
    try:
        invoices_details = Invoice_details.objects.filter(invoice__id=invoice_id)
        if len(invoices_details) == 0:
            # TODO:Return failure response
            invoices_detail = None
            raise Invoice_details.DoesNotExist 
        else:
            invoices_detail = invoices_details[0]
    except Invoice_details.DoesNotExist:
        invoices_detail = None
    if request.method=='GET':
        print("invoices_detail was ", invoices_detail)
        if invoices_detail == None:
            detailsObj = Invoice_details()
            serializer=InvoicedetailSerializer(detailsObj,many=False)
        else:
            serializer=InvoicedetailSerializer(invoices_detail,many=False)
        return Response(serializer.data,status.HTTP_200_OK)
       
    elif request.method=='PUT':
        #update and if resource is not present it will create it
        if invoices_detail is None:
            # TODO:Incase of invoice details are missing return failure response
            pass
        
        invoices_detail.description=request.data['description']
        invoices_detail.quantity=request.data["quantity"]
        invoices_detail.unit_price=request.data["unit_price"]
        invoices_detail.save()
        serializer=InvoicedetailSerializer(invoices_detail)
        return Response(serializer.data,status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = InvoicedetailSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
       
    if request.method=='DELETE':
        invoices_details.delete()
        return Response("DONE",status.HTTP_200_OK)
            
   