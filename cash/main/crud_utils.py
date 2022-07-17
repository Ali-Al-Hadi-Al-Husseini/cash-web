from .models import Balance,Transcation
from datetime import datetime

def query_balacne(owener,currency):
    return Balance.objects.filter(owner=owener.id,currency_type=currency)

def update_balance(balance,amount):
    current_amount = balance.values()[0]["amount"]
    balance.update(amount=current_amount + amount)

def valdidate_tansaction(balance, amount,pin):
    if balance['amount'] > amount:
        if balance['pay_pin'] == pin:
            return True ,""
        else:
            return 'pay_pin'
        
    return False ,"amount"

def transact_money(sender_balance,rec,amount,currency):
    rec_balance = query_balacne(rec,currency)
    update_balance(sender_balance,-amount) 
    update_balance(rec_balance,amount)


def create_balances(owner,pay_pin):
    USD_balance = Balance.objects.create(amount=1_000_000,
                                        pay_pin=pay_pin,
                                        currency_type = "USD",
                                        owner = owner,
                                        )
    LB_balance = Balance.objects.create(amount=0,
                                        pay_pin=pay_pin,
                                        currency_type = "LB",
                                        owner = owner,
                                        )
def get_transactions(user):
    sent_transactionss = Transcation.objects.filter(sender = user )
    reciever_transactions = Transcation.objects.filter(reciever = user )

    all_transactions =  reciever_transactions | sent_transactionss
    all_transactions = all_transactions.order_by('-id')[:5]

    return all_transactions.values()

def get_transactions_time(transcation):
    created_time  = transcation['date_time'][2:19]
    now = str(datetime.now())[2:19]
    time_ago = subtract_time (created_time , now)
    return time_ago

def subtract_time(date_time,date_time2):
    date, time = date_time.split(' ')
    date2, time2 = date_time2.split(' ')

    years_differnce = abs( int(date[:2]) - int(date2[:2]))

    if years_differnce == 0:
        months_differnce = abs( int(date[3:5]) - int(date2[3:5]))

        if months_differnce == 0:
            days_differnce = abs( int(date[6:-1]) - int(date2[6:-1]))

            if days_differnce == 0 :  
                hours_differnce = abs( int(time[:2]) - int(time2[:2]))

                if hours_differnce == 0:
                    mins_differnce = abs( int(time[3:5]) - int(time2[3:5]))

                    if mins_differnce == 0:
                        secs_differnce = abs( int(date[6:-1]) - int(date2[6:-1]))

                        return str(secs_differnce) + 'sec'

                    return str(mins_differnce) + ' min'

                return str(hours_differnce) + ' hour'

            return str(days_differnce) + " day" 

        return str(months_differnce) + " month"

    return str(years_differnce) + " years"

def reformat_transasctions(transction):
    pass