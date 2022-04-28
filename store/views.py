from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from store.models.product import Product
# Create your views here.
def index(request):
    prds=Product.get_all_products();

   # return  render(request, 'orders/order.html')
    return render(request, 'index.html',{'products' : prds})

    # print(products)

    # return render(request, 'orders/order.html')