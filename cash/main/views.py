from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def main(req):
    return render(req,"main/index.html",{})


def signUp(req):
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(req,'registration/signup.html',{'form':form})
