from locale import currency
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 

class Balance(models.Model):
    amount = models.IntegerField()
    pay_pin = models.IntegerField()

    currency_type = models.CharField(max_length=4)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

class Transcation(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciever")

    date_time = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.sender} sent {self.amount} to {self.receiver}"
    


    

