# Generated by Django 5.0.3 on 2024-11-14 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0007_delete_about_delete_itemportfolio_delete_shares_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddPortfolio',
        ),
        migrations.DeleteModel(
            name='DeletePortfolio',
        ),
        migrations.DeleteModel(
            name='General',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='StockData',
        ),
    ]
