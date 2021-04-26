from django.shortcuts import render, redirect
from django.views.generic.edit import FormView 
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from .models import Fcuser

# Create your views here.

def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'  

    def form_valid(self,form):     # form_valid 함수를 오버라이딩 
        fcuser = Fcuser(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')), 
            level = 'user'
        )
        fcuser.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'  

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')  # form_valid 함수를 통과하면 이 조건 실행 
        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')