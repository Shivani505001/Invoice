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

# Create your views here.


def front(request):
   return render(request,'base.html')
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
        
    
@api_view(['GET','PUT','DELETE'])
def details(request,pk):
    try:
        invoices=Invoice_details.objects.get(pk=pk)
    except Invoice_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    # invoices=Invoice_details.objects.get(pk=pk)
    if request.method=='GET':
        serializer=InvoicedetailSerializer(invoices,many=False)
        return Response(serializer.data,status.HTTP_200_OK)
       
    elif request.method=='PUT': #update and if resource is not present it will create it
        
        invoices.description=request.data['description']
        invoices.quantity=request.data["quantity"]
        invoices.unit_price=request.data["unit_price"]
        invoices.save()
        serializer=InvoicedetailSerializer(invoices)
        return Response(serializer.data,status.HTTP_200_OK)
   
       
    if request.method=='DELETE':
        invoices.delete()
        return Response("DONE",status.HTTP_200_OK)
            
   