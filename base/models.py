from django.db import models

# Create your models here.

class Invoices(models.Model):
    date=models.DateField(auto_now=True)
    name=models.CharField(max_length=200,blank=False)
    
    def __str__(self) :
        return self.name

class Invoice_details(models.Model):
    invoice=models.ForeignKey(Invoices,on_delete=models.CASCADE)
    description=models.CharField(max_length=300,blank=False)
    quantity=models.PositiveIntegerField(blank=False) #quantity is always positive 
    unit_price=models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Calculate the price before saving
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)