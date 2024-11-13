from django import forms
from .models import AddPortfolio, DeletePortfolio, StockData, History



# stock_choices=[
#     ('0', 'Click Here to Select a Stock'),
#     ('1', 'Microsoft - $452.16/share'),
#     ('2', 'Google - $185.37/share'),
#     ('3', 'GE - $160.64/share'),
#     ('4', 'Amazon - $193.61/share'),
# ]

# quantity_choices=[
#     ('0', 'Click Here to Select a Quantity'),
#     ('1', '1'),
#     ('2', '2'),
#     ('3', '3'),
#     ('4', '4'),
#     ('5', '5'),
#     ('6', '6'),
#     ('7', '7'),
#     ('8', '8'),
#     ('9', '9'),
#     ('10', '10'),
# ]

# price_choices=[
#     ('0', 'Click Here to Select a Stock'),
#     ('1', 'Microsoft - $452.16/share'),
#     ('2', 'Google - $185.37/share'),
#     ('3', 'GE - $160.64/share'),
#     ('4', 'Amazon - $193.61/share'),
# ]

# dollar_choices=[
#     ('0', 'Click Here to Select a Stock'),
#     ('1', 'Microsoft - $452.16/share'),
#     ('2', 'Google - $185.37/share'),
#     ('3', 'GE - $160.64/share'),
#     ('4', 'Amazon - $193.61/share'),
# ]


# msft_choices=[
#     ('0', '452.16'),
# ]
# amzn_choices=[
#     ('0', '193.61'),
# ]
# ge_choices=[
#     ('0', '160.64'),
# ]
# goog_choices=[
#     ('0', '185.37'),
# ]

# table_choices=[
#     ('stock', 'Stock'),
#     ('open', 'Open'),
#     ('high', 'High'),
#     ('low', 'Low'),
#     ('close', 'Close'),
# ]

# class registrationform(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)


# class AddPortfolioForm(forms.ModelForm):
#     class Meta:
#         model = AddPortfolio
#         fields = ('stock', 'quantity')

#         widgets = {
#             'stock': forms.Select(choices=stock_choices, attrs={'class': 'form-control'}),
#             'quantity': forms.Select(choices=quantity_choices, attrs={'class': 'form-control'}),
#         }


# class DeletePortfolioForm(forms.ModelForm):
#     class Meta:
#         model = DeletePortfolio
#         fields = ('stock', 'quantity')
 
#         widgets = {
#             'stock': forms.Select(choices=stock_choices, attrs={'class': 'form-control'}),
#             'quantity': forms.Select(choices=quantity_choices, attrs={'class': 'form-control'}),
#         }


# class StockDataForm(forms.ModelForm):
#     class Meta:
#         model = StockData
#         fields = ('stock',)

#         widgets = {
#             'stock': forms.Select(choices=stock_choices, attrs={'class': 'form-control'}),
#          } 


# class HistoryForm(forms.ModelForm):
#     class Meta:
#         model = History
#         fields = ('stock',)

#         widgets = {
#             'stock': forms.Select(choices=stock_choices, attrs={'class': 'form-control'}),
#          } 


