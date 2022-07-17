from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transcation

class RegistrationForm (UserCreationForm):
    email= forms.EmailField (required=True)
    pay_pin = forms.IntegerField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", 'pay_pin',"password1", "password2"]


class TransactionForm(forms.ModelForm):
    pay_pin = forms.IntegerField(required=True)
    currency_type = forms.CharField(required=True,max_length=4)
    class  Meta:
        model = Transcation
        fields = ['amount','reciever','pay_pin',"currency_type"]