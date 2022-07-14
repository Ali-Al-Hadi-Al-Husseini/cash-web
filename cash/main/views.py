from django.shortcuts import render, redirect
from .forms import RegistrationForm, TransactionForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def main(req):
    form, form_is_valid = validate_form(req,TransactionForm)
    if form_is_valid:
        transaction = form.save(commit=False)
        transaction.sender = req.user
        transaction.save() 
        return redirect("/")
    return render(req,"main/index.html",{'form':form})

def signUp(req):
    form , form_is_valid = validate_form(req, RegistrationForm)
    if form_is_valid:
        user = form.save()
        login(req,user)
        return redirect("/")

    return render(req,'registration/signup.html',{'form':form})

def validate_form(req,form_type):
    if req.method == "POST":
        form = form_type(req.POST)
        if form.is_valid():
            return form,True
    else:
        form = form_type()
    
    return form,False