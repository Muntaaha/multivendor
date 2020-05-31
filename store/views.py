from django.shortcuts import render, redirect
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
    products = Product.objects.all()
    context = {'products':products}
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
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'store/cart.html',context)

@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'store/checkout.html',context)
