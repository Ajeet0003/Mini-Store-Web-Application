from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from store.models.product import Product
from store.models.category import Category
# Create your views here.
def index(request):
    products=None
    categories=Category.get_all_categories()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.get_all_product_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data={}
    data['products']=products
    data['categories']=categories
    return render(request, 'index.html',data)

  #  def signup(request d ):
      #  return render(request, 'signup.html')
    # return  render(request, 'orders/order.html')
    # print(products)

    # return render(request, 'orders/order.html')
def signup(request):
    return render(request,'signup.html')