from django import forms
from core.models import UserProfileInfo
from django.contrib.auth.models import User

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('fn','ln','ads','portfolio_site','profile_pic')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')