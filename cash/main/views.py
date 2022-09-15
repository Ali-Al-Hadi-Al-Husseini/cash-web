from django.shortcuts import render, redirect
from .forms import RegistrationForm, TransactionForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import create_balances, validate_form,validate_tansaction, transact_money, query_balance, get_transactions
from django.contrib import messages
# Create your views here.

@login_required(login_url="/login")
def main(req):
    args = {}
    usd_balance = query_balance(req.user,'USD').values()[0]
    lb_balance = query_balance(req.user,'LB').values()[0]
    transactions = get_transactions(req.user.id)
    
    args['transactions'] = transactions
    args["id"] = req.user.id

    args['lb_balance'] = lb_balance["amount"]
    args['usd_balance'] = usd_balance["amount"]

    args['lb_qrcode'] = f"{req.user}_--_LB"
    args['usd_qrcode'] = f"{req.user}_--_USD"

    return render(req,"main/index.html",args)

@login_required(login_url="/login")
def transact(req):
    authenticate(req)
    form, form_is_valid = validate_form(req,TransactionForm)

    if form_is_valid:
        transaction = form.save(commit=False)
        transaction.sender = req.user
        sender_balance = query_balance(req.user,transaction.currency_type)

        transaction_is_valid , transaction_error = validate_tansaction(
                                                            req.user.id,
                                                            sender_balance.values()[0] ,
                                                            transaction.amount,
                                                            form.cleaned_data['pay_pin'],
                                                            transaction.receiver
                                                            )

        if transaction_is_valid:

            transact_money(sender_balance,transaction.receiver,transaction.amount,transaction.currency_type)
            transaction.date_time = datetime.now()
            transaction.save() 

            messages.success(req, f"{transaction.amount} {transaction.currency_type} was sent to {transaction.receiver} successfully")
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



