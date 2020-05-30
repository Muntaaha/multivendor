from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('store')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('Working: ', allowed_roles)
            
            if allowed_roles=="customer":
                usr = request.user
                if Customer.objects.get(user=usr) 
                return view_func(request, *args, **kwargs)

            
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
            else:
                return render(request,'store/decorator.html', {} )

                
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator