# Generated by Django 4.1.13 on 2024-01-27 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_invoice_details_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_details',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.invoices'),
        ),
    ]
