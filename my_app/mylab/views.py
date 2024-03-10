from django.shortcuts import render
from django.http import HttpResponse
tax_rate = 15

def default(request):
    return render(request, 'mylab/default.html')

def taxrate(request):
    return HttpResponse ("Tax Rate: 15%")

def anyNumber(request, price):
    price = float(price)
    total = price + (price * tax_rate * 0.01)
    return render(request, 'mylab/anyNumber.html', {'total': total})
