from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password,check_password


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_product_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)

# def sign_up(request):
#     fm=UserCreationForm()
#     return  render(request,'ministore/signup.html',{'form':fm})



#  def signup(request):
#  return render(request, 'signup.html')
# return  render(request, 'orders/order.html')
# print(products)
#
# return render(request, 'orders/order.html')
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        # phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        #    # postData=request.POST
        # first_name = request.POST.get('firstname')
        # last_name = request.POST.get('lastname')
        # phone = request.POST.get('phone')
        # email = request.POST.get('email')
        # password = request.POST.get('password')

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            # phone=phone,
                            email=email,
                            password=password)

    customer.password=make_password(customer.password)
    customer.register()
    return redirect('homepage')
    # return HttpResponse("signup success")
    # return render(request,'signup.html')
# print(first_name,last_name)

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        print(email, password)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message='email or password invalid'
        else:
            error_message='email or password invalid'
        return render(request,'login.html',{'error':error_message})

