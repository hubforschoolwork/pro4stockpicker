from django.contrib import admin
from .models import ItemPortfolio,TransactionHistory, AddPortfolio, DeletePortfolio, StockData, History






admin.site.register(ItemPortfolio)
admin.site.register(TransactionHistory)
admin.site.register(AddPortfolio)
admin.site.register(DeletePortfolio)
admin.site.register(StockData)
admin.site.register(History)



