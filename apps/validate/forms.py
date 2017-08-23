# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 03 17:37
# Author Yo
# Email YoLoveLife@outlook.com
from django import forms
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(forms.Form):
    username=forms.CharField(label="用户名",max_length=100,widget=forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'账户'}))
    passwd=forms.CharField(label="密码",widget=forms.PasswordInput(attrs={'type':'password','class':'form-control','placeholder':'密码'}))