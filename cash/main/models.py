from django.db import models
from django.contrib.auth.models import User


currencies = [('USD',"$"),('LB','L.L.')]

class Balance(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    pay_pin = models.CharField(max_length=100,default="9sk#atg243%@#")
    salt = models.CharField(max_length=100,default="9sk#atg243%@#")

    currency_type = models.CharField(max_length=4)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    # qr_code = models.ImageField(upload_to=MEDIA_ROOT)


class Transcation(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver")

    date_time = models.CharField(max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    currency_type = models.CharField(max_length=4,choices=currencies)

    def __str__(self) -> str:
        return f"{self.sender} sent {self.amount} to {self.receiver}"
    

    

