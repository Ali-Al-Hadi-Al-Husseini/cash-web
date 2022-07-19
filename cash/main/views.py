from distutils.log import error
from urllib import request
from django.shortcuts import render, redirect
from .forms import RegistrationForm, TransactionForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import create_balances, validate_form,validate_tansaction, transact_money, query_balacne, get_transactions
from django.contrib import messages
# Create your views here.
@login_required(login_url="/login")
def main(req):

    transactions = get_transactions(req.user.id)
    args = {}
    args['transactions'] = transactions
    

    return render(req,"main/index.html",args)

@login_required(login_url="/login")
def transact(req):
    form, form_is_valid = validate_form(req,TransactionForm)

    if form_is_valid:
        transaction = form.save(commit=False)
        transaction.sender = req.user
        sender_balance = query_balacne(req.user,transaction.currency_type)

        transaction_is_valid , transaction_error = validate_tansaction(
                                                            req.user.id,
                                                            sender_balance.values()[0] ,
                                                            transaction.amount,
                                                            form.cleaned_data['pay_pin'],
                                                            transaction.reciever
                                                            )

        if transaction_is_valid:

            transact_money(sender_balance,transaction.reciever,transaction.amount,transaction.currency_type)
            transaction.date_time = datetime.now()
            transaction.save() 

            messages.success(req, f"{transaction.amount} {transaction.currency_type} was sent to {transaction.reciever} successfully")
            return redirect("/transact")
        
        messages.warning(req, transaction_error)

    return render(req,"main/transact.html",{'form':form})

def signUp(req):
    form , form_is_valid = validate_form(req, RegistrationForm)
    if form_is_valid:
        pay_pin = form.cleaned_data['pay_pin']
        del form.cleaned_data['pay_pin']
        
        user = form.save()

        create_balances(user,pay_pin)
        login(req,user)

        return redirect("/")

    return render(req,'registration/signup.html',{'form':form})



