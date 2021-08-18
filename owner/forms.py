from django import forms

class SignupForm(forms.Form):
    firstname=forms.CharField()
    username=forms.CharField()
    email=forms.CharField()
    password1=forms.CharField()
    confirmpassword=forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class MobileAdd(forms.Form):
    mob_name = forms.CharField()
    color = forms.CharField()
    memory = forms.IntegerField()
    camera = forms.IntegerField()
    price=forms.IntegerField()

