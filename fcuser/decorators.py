from django.shortcuts import redirect
from .models import Fcuser

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            print('login required')
            return redirect('/login')
        return function(request, *args, **kwargs)
    return wrap 

def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = Fcuser.objects.get(email=user)
        if user.level != 'admin':
            print(user)
            return redirect('/')

        return function(request, *args, **kwargs)
    return wrap 