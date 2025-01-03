from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('registrationform', views.registrationform, name='registrationform'),
    path('general', views.general, name='general'),
    path('amazon', views.amazon, name='amazon'),
    path('microsoft', views.microsoft, name='microsoft'),
    path('google', views.google, name='google'),
    path('stock_data_amazon', views.stock_data_amazon, name='stock_data_amazon'),
    path('stock_data_ge', views.stock_data_ge, name='stock_data_ge'),
    path('stock_data_google', views.stock_data_google, name='stock_data_google'),
    path('stock_data_microsoft', views.stock_data_microsoft, name='stock_data_microsoft'),
    path('display_selection/', views.display_selection, name='display_selection'),
    path('display_sells/', views.display_sells, name='display_sells'),
    path('sellform', views.sellform, name='sellform'),

    path('stock_data', views.stock_data, name='stock_data'),
    path('historical_data', views.historical_data, name='historical_data'),
    path('add_portfolio', views.add_portfolio, name='add_portfolio'),
    path('delete_portfolio', views.delete_portfolio, name='delete_portfolio'),


]


