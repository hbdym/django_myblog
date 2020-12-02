# 引入表单类
from django import forms
# 引入user
from django.contrib.auth.models import User

# 登录表单，继承forms.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
