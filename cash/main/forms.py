from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transcation
from .constants import temp_email_domains , Currencies
from .utils import query_user

class RegistrationForm (UserCreationForm):
    email= forms.EmailField (required=True)
    pay_pin = forms.CharField(required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        domain = email.split("@")[1]

        if domain in temp_email_domains:
            raise forms.ValidationError("You can't use a temporary email address")
        return email
    
    def clean_pay_pin(self):
        pay_pin = self.cleaned_data.get('pay_pin')
        int_str = str(pay_pin)

        if len(int_str) < 6:
            raise forms.ValidationError("Pay-pin should be aleast 6-digits")
        return pay_pin
        
    class Meta:
        model = User
        fields = ["username", "email", 'pay_pin',"password1", "password2"]


class TransactionForm(forms.ModelForm):
    pay_pin = forms.CharField(required=True)
    amount = forms.DecimalField(required=True,min_value=0)

    def clean_currency_type(self):
        currency = self.cleaned_data.get("currency_type")

        if currency not in Currencies:
            raise forms.ValidationError("You can only send LB or USD")

        return currency


    class  Meta:
        model = Transcation
        fields = ['amount','receiver','pay_pin',"currency_type"]


