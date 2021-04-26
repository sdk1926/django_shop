from django import forms
from .models import Order 
from fcuser.models import Fcuser
from product.models import Product
from django.db import transaction

class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)           # form에 request를 전달 받기 위해 만들었다. 
        self.request = request
        

    quantity = forms.IntegerField(
        error_messages={
            'required' : '수량을 입력해주세요.'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required' : '상품가격을 입력해주세요.'
        }, label='상품가격', widget=forms.HiddenInput # 화면에는 보이지 않는 인풋
    )
   

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        

        if not (quantity and product):                        
            self.add_error('quantity', '수량을 입력해주세요')
            self.add_error('product', '값을 입력해주세요.')
    