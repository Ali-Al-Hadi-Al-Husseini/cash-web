from locale import currency
from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=50,default=email)
    
    password_hash = models.CharField(max_length=100)
    
class Balance(models.Model):
    amount = models.IntegerField()
    pay_pin = models.IntegerField()

    currency_type = models.CharField(max_length=4)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

class Transcation(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciever")

    date_time = models.CharField(max_length=50)
    amount = models.IntegerField()
    


    

