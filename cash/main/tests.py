from django.test import TestCase
from .testing_utils import create_user,create_trans
from .utils import transact_money,query_balance,get_transactions_value,subtract_time
from random import randrange
from .hashing import hash_with_salt
# Create your tests here.

class user_generation(TestCase):
    
    def setUp(self) -> None:
        self.number_of_users = 100
        self.senders = [create_user() for _ in range(self.number_of_users)]

class balance_test(user_generation):

    def test_balance_creation(self):
        for user in self.senders:
    
            for currency in ['LB','USD']:
                balance = query_balance(user[0],currency=currency)
                balance = balance.values()[0]
                salt = balance['salt']
                _ , pay_pin = hash_with_salt(user[1]['pay_pin'],salt)

                self.assertEqual(balance['pay_pin'],pay_pin)
                self.assertEqual(balance['amount'] , 100)
                

class Transaction_test(user_generation):
    
    def test_transction(self):
        for idx in range(self.number_of_users):
            amount = randrange(0,11)
            currency = 'USD' if randrange(0,2) == 0 else "LB"
            sender,_ = self.senders[idx]
            reciever,_ = self.senders[self.number_of_users-1-idx]  
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

            # test to see if transaction added to database
            transaction = get_transactions_value(sender)[0]

            self.assertEqual(transaction['amount'],amount)
            self.assertEqual(transaction['currency_type'],currency)
            self.assertEqual(transaction['sender_id'],sender.id)
            self.assertEqual(transaction['receiver_id'],reciever.id)

            
            
class Subtract_time_test(TestCase):

    def test_subtract_time(self):
        test_cases = [
                ('21-09-12 00:23:43.104102','22-09-12 00:23:43.104102','1 year ago'),
                ('22-09-11 00:23:43.104102','22-09-12 00:23:43.104102','1 day ago'),
                ('22-08-12 00:23:43.104102','22-09-12 00:23:43.104102','1 month ago'),
                ('22-09-12 00:23:43.104102','22-09-12 01:23:43.104102','1 hour ago'),
                ('20-09-12 00:23:43.104102','22-09-12 00:23:43.104102','2 years ago'),
                ('22-09-09 00:23:43.104102','22-09-12 00:23:43.104102','3 days ago'),
                ('22-05-12 00:23:43.104102','22-09-12 00:23:43.104102','4 months ago'),
                ('22-09-12 00:23:43.104102','22-09-12 10:23:43.104102','10 hours ago'),
        ]
        
        for start,end,expected_result in test_cases:
            result = subtract_time(start,end)

            self.assertEqual(result,expected_result)




