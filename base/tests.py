from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Invoices, Invoice_details


class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        # Create some initial data for testing
        self.invoice = Invoices.objects.create(name="Test1")
        self.invoice_detail = Invoice_details.objects.create(
            invoice=self.invoice,
            description="Test1 des",
            quantity=2,
            unit_price=10.00,
            price=20.00
        )
        
    def test_all_invoices(self):
            # Test GET /invoices/
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test POST /invoices/
        data = {'name': 'New Invoice'}
        response = self.client.post('/invoices/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        #edge case where the name feild is empty
        data = {'name': ''}
        response = self.client.post('/invoices/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test DELETE /invoices/ (corrected to provide pk and expect 200)
        url = reverse('all-invoices')
        response = self.client.delete(url, data={'pk': self.invoice.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #trying to delete all invoices without providing pk
        url = reverse('all-invoices')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_details(self):
        self.invoice = Invoices.objects.create(name="Test1")
        # Test GET request
        url = reverse('invoice-detail', args=[self.invoice.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       
        #Test POST request
        new_data = {'invoice': self.invoice.id, 'description': 'New Item', 'quantity': 1, 'unit_price': 5}
        url = reverse('invoice-detail', args=[self.invoice.id])  
        response = self.client.post(url, data=new_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test DELETE request
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
