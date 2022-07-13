from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(requesrt):
    return render(requesrt,"main/index.html",{})