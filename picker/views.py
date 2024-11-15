# from django.views.generic import ListView, CreateView, DeleteView
# from picker.templatetags.custom_filters import extract_number

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import re


def display_selection(request):
    if request.method == "POST":
        selected_item = request.POST.get('selected_item')

        # Initialize the session variable if it doesn't exist
        if 'submitted_items' not in request.session:
            request.session['submitted_items'] = []

        # Append the selected item to the session list
        if selected_item:
            submitted_items = request.session['submitted_items']
            submitted_items.append(selected_item)
            request.session['submitted_items'] = submitted_items

         # Pass the running list to the template
        return render(request, 'registrationform.html', {'submitted_items': request.session['submitted_items']})

    # return render(request, 'add_portfolio.html')

# **********************************************************************************

def display_sells(request):
    if request.method == "POST":
        sells_item = request.POST.get('sells_item')

        # Initialize the session variable if it doesn't exist
        if 'chosen_items' not in request.session:
            request.session['chosen_items'] = []

        # Append the selected item to the session list
        if sells_item:
            chosen_items = request.session['chosen_items']
            chosen_items.append(sells_item)
            request.session['chosen_items'] = chosen_items

         # Pass the running list to the template
        return render(request, 'sellform.html', {'chosen_items': request.session['chosen_items']})

    # return render(request, 'add_portfolio.html')


def home(request):
    return render(request, 'home.html', {})

def sellform(request):
    return render(request, 'sellform.html', {})

def historical_data(request):
    return render(request, 'historical_data.html', {})

def stock_data(request):
    return render(request, 'stock_data.html', {})

def add_portfolio(request):
    return render(request, 'add_portfolio.html', {})

def delete_portfolio(request):
    return render(request, 'delete_portfolio.html', {})

def registrationform(request):
    return render(request, 'registrationform.html', {})

def general(request):
    return render(request, 'general.html', {})

def amazon(request):
    return render(request, 'amazon.html', {})

def google(request):
    return render(request, 'google.html', {})

def microsoft(request):
    return render(request, 'microsoft.html', {})

def stock_data_amazon(request):
    return render(request, 'stock_data_amazon.html', {})

def stock_data_ge(request):
    return render(request, 'stock_data_ge.html', {})

def stock_data_google(request):
    return render(request, 'stock_data_google.html', {})

def stock_data_microsoft(request):
    return render(request, 'stock_data_microsoft.html', {})

