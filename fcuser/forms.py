from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        # super()는 메소드 오버라이딩 
        cleaned_data = super().clean()  # 값이 들어있는지 검사한다. 들어잇으면 아래 변수를 할당, 없으면 실패하고 튕군다. 
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
           

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    
    def clean(self):
        # super()는 메소드 오버라이딩 
        cleaned_data = super().clean()  # 값이 들어있는지 검사한다. 들어잇으면 아래 변수를 할당, 없으면 실패하고 튕군다. 
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)
            except Fcuser.DoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
           
