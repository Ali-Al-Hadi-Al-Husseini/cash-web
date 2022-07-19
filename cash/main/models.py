from locale import currency
from django.db import models
from django.contrib.auth.models import User

currencies = [('USD',"$"),('LB','L.L.')]

class Balance(models.Model):
    amount = models.IntegerField()
    pay_pin = models.IntegerField()

    currency_type = models.CharField(max_length=4)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)


class Transcation(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    # databases needs to be rested to fix this spelling mistake
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciever")

    date_time = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    currency_type = models.CharField(max_length=4,choices=currencies)

    def __str__(self) -> str:
        return f"{self.sender} sent {self.amount} to {self.reciever}"
    

    

