from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm
from product.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            form.save()
            return redirect('login')
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for '+user)

    context = {'form':form}
    return render(request, 'store/register.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html',context)

def user_profile(request):
    context = {}
    return render(request,'store/user_profile.html', context )


def cart(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitems_set.all()
    # else:
    #     items = []
    context = {}
    return render(request,'store/cart.html',context)


def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
