# Generated by Django 5.0.3 on 2024-11-14 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0006_general_shares'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='ItemPortfolio',
        ),
        migrations.DeleteModel(
            name='Shares',
        ),
        migrations.DeleteModel(
            name='Ticker',
        ),
        migrations.DeleteModel(
            name='TransactionHistory',
        ),
    ]
