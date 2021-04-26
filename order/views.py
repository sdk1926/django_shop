from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator # 클래스에 데모레이터 붙이게 해주는 녀석 
from fcuser.decorators import login_required
from .forms import RegisterForm 
from .models import Order
from django.db import transaction
from product.models import Product
from fcuser.models import Fcuser

# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView): 
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=form.data.get('quantity'),
                product=prod,               # 주문한 상품의 객체를 주문모델의 상품필드에 저장         
                fcuser=Fcuser.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))  # forms.py에서 self.product = product product는 html태그에서 value값이 id값이므로 숫자가 넘어간다.


    def get_form_kwargs(self, **kwargs):   # 폼을 생성할 떄 어떤 인자값을 전달해줄지 알려주는 함수 
        kw = super().get_form_kwargs(**kwargs)  
        kw.update({
            'request': self.request      # 기존에 생성된 인자값에 request를 추가해준다. 
        })
        return kw 

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html' 
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):  # queryset을 오버라이딩해서 로그인한 사람의 정보만 표시하게 한다. 
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset