from django.test import TestCase
from .testing_utils import create_user,create_trans
from .utils import transact_money,query_balance
from random import randrange
# Create your tests here.

class Transaction_test(TestCase):

    def setUp(self) -> None:
        self.number_of_users = 100
        self.senders = [create_user() for _ in range(self.number_of_users)]


    def test_transction(self):
        for idx in range(self.number_of_users):
            amount = randrange(0,11)
            currency = 'USD' if randrange(0,2) == 0 else "LB"
            sender = self.senders[idx]
            reciever = self.senders[self.number_of_users-1-idx]  
            sen_balance = query_balance(sender,currency)
            rec_balance = query_balance(reciever,currency)
            sen_amount = sen_balance.values()[0]["amount"]
            rec_amount = rec_balance.values()[0]["amount"]

            create_trans(sender,reciever,amount,currency)
            transact_money(sen_balance,reciever,amount,currency)

            sen_values = sen_balance.values()[0]
            rec_values = rec_balance.values()[0]

            self.assertEqual(sen_amount- amount ,sen_values['amount'])
            self.assertEqual(rec_amount+ amount ,rec_values['amount'])






