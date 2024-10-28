from django.urls import path
from . import views
from .views import ItemPortfolioView, AddPortfolioView, DeletePortfolioView, HistoryView, StockDataView, TransactionHistoryView, GeneralView, AmazonView, MicrosoftView, GoogleView, Stock_Data_AmazonView, display_selection
from .views import display_selection, display_sells, sellform



urlpatterns = [
    path('', views.home, name="home"),
    path('item_portfolio', ItemPortfolioView.as_view(), name='item_portfolio'),
    path('stock_data', StockDataView.as_view(), name='stock_data'),
    path('transaction_history', TransactionHistoryView.as_view(), name='transaction_history'),
    path('historical_data', HistoryView.as_view(), name='historical_data'),
    path('add_portfolio', AddPortfolioView.as_view(), name='add_portfolio'),
    path('delete_portfolio', DeletePortfolioView.as_view(), name='delete_portfolio'),
    # path('test', views.test, name='test'),
    path('registrationform', views.registrationform, name='registrationform'),
    path('general', views.general, name='general'),
    path('amazon', views.amazon, name='amazon'),
    path('microsoft', views.microsoft, name='microsoft'),
    path('google', views.google, name='google'),
    path('stock_data_amazon', views.stock_data_amazon, name='stock_data_amazon'),
    path('stock_data_ge', views.stock_data_ge, name='stock_data_ge'),
    path('stock_data_google', views.stock_data_google, name='stock_data_google'),
    path('stock_data_microsoft', views.stock_data_microsoft, name='stock_data_microsoft'),
    path('display_selection/', display_selection, name='display_selection'),
    path('display_sells/', display_sells, name='display_sells'),
    path('sellform', sellform, name='sellform'),
  
]


