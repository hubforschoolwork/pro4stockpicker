from django.db import models
# from django.contrib.auth.models import User




class General(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)


# Total Portfolio Valuation
class ItemPortfolio(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    current_total_value = models.DecimalField(max_digits=5, decimal_places=2)
    current_price = models.DecimalField(max_digits=5, decimal_places=2)

# Transaction History
class TransactionHistory(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)

# To purchase stock
class AddPortfolio(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)


# To sell off stock
class DeletePortfolio(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

# To view current data
class StockData(models.Model):
    stock = models.CharField(max_length=10)

# To view historical stock data inside or outside portfolio:  chart
class History(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)





    

