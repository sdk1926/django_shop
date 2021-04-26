from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins
from fcuser.decorators import admin_required
from .models import Product
from .forms import RegisterForm
from .serializers import ProductSerializer
from order.forms import RegisterForm as OrderForm
# Create your views here.

class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request , *args , **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request , *args , **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductList(ListView):
    model = Product
    template_name = 'product.html' 
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
                name=form.data.get('name'),
                price=form.data.get('price'),
                description=form.data.get('description'),
                stock=form.data.get('stock')
            )
        product.save()
        
        return super().form_valid(form)
    
class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()   # 모든 제품에서 하나씩 꺼내서 쓸 것이기에 queryset을 쓴다. 
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = OrderForm(self.request)  # orderform에서 받은 값을 'form'으로 템플릿에 전달한다. 
        return context                             # view 함수이기 때문에 request가 있으니 폼을 생성할 때 request를 전달한다. 
