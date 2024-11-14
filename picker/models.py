from django.db import models
from django.contrib.auth.models import User


class General(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)


class AddPortfolio(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

class DeletePortfolio(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

class StockData(models.Model):
    stock = models.CharField(max_length=10)

class History(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)





    


