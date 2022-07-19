from .models import Balance,Transcation, User
from datetime import datetime

def query_balacne(owener,currency):
    return Balance.objects.filter(owner=owener.id,currency_type=currency)

def query_user(id):
    return User.objects.filter(id= id).values()[0]

def update_balance(balance,amount):
    current_amount = balance.values()[0]["amount"]
    balance.update(amount=current_amount + amount)

def validate_tansaction(sender_id,balance, amount,pin, rec):
    if sender_id == rec.id:
        return False , "Can't send money to your self"
    if balance['amount'] > amount:
        if balance['pay_pin'] == pin:
            return True ,""
        else:
            return False,'Pay-Pin is not correct'
        
    return False ,"You dont have enough money!"

def transact_money(sender_balance,rec,amount,currency):
    rec_balance = query_balacne(rec,currency)
    update_balance(sender_balance,-amount) 
    update_balance(rec_balance,amount)



def get_transactions_value(user):
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

                        return pluralize(secs_differnce , ' sec')

                    return pluralize(mins_differnce , ' min')

                return pluralize(hours_differnce , ' hour')

            return pluralize(days_differnce , " day" )

        return pluralize(months_differnce, " month")

    return pluralize(years_differnce , " year")

def pluralize(num,date):
    if date == ' sec' and num == 0 : return 'Now'
    if num > 1 : return str(num) + date + "s" + ' ago'
    return str(num) +  date +' ago'

def reformat_transasctions(transction,user):
    return  [
            transction['sender_id'],
            get_transactions_time(transction),
            transction['amount'],
            transction['currency_type'],
            transction["reciever_id"],
            user == transction['sender_id']

    ]

def get_transactions(user):
    transactions_value = get_transactions_value(user)
    reformated_transactions = []

    for values in transactions_value:
        reformated_transactions.append(reformat_transasctions(values,user))

    return reformated_transactions