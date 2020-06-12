from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from .forms import RegistrationForm

from product.models import *
from order.models import *
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request,'Username and Password is not valid')
    context = {}
    return render(request, 'store/login.html', context)


def user_register(request):
    form = RegistrationForm()

    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password1)
                instance = form.save(commit=False)
                instance.user = user
                instance.save()

                messages.success(request, 'Account has been created for '+username)
                return redirect('login')

    context = {'form':form}
    return render(request, 'store/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}


    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems, 'shipping': False}
    return render(request,'store/store.html',context)

@login_required(login_url='login')
def user_profile(request):
    context = {}
    return render(request,'store/user_profile.html', context )

@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'shipping': False}
    return render(request,'store/cart.html',context)

@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'shipping': False}
    return render(request,'store/checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    return JsonResponse('Payment Completed', safe=False)