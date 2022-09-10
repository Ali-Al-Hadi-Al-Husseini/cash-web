import random
from datetime import datetime
from django.contrib.auth.models import User
from .utils import create_balances
from .models import Transcation

chars_numbers = '1234567890qwertyuiopasdfghjklzxcvbnm'

def generate_random_str():
    return  ''.join(random.choices(chars_numbers, k = 10))


def generate_email():
    return generate_random_str() + '@Mymail.com'

# ["username", "email", 'pay_pin',"password1", "password2"]
def create_user():
    usr = {
        'username': generate_random_str(),
        'email':generate_email(),
        'pay_pin': generate_random_str(),
        'password': generate_random_str()

    } 

    
    user = User.objects.create(username=usr['username'],email=usr['email'],password=usr['password'])
    create_balances(user,usr['pay_pin'])
    return user

def create_trans(sen,rec,am,cur):
    return Transcation.objects.create(sender=sen,receiver=rec,date_time=datetime.now(),amount=am,currency_type=cur)