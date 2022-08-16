import qrcode
from .crud_utils import *
from .constants import Currencies
from .hashing import hash_with_salt

# def make_qr(owner,currency):
#     data = owner + "_--_" + currency
#     qr = qrcode.QRCode(version=1,
#                        box_size=8,
#                        border=5)

#     qr.add_data(data)
#     qr.make(fit=True)
#     img = qr.make_image()

#     return img.save()


# def make_qrcodes(owner_id):
#     qrcodes = []
#     for currency in Currencies:
#         qrcodes.append(make_qr(str(owner_id), currency))

#     return qrcodes

def create_balances(owner,pay_pin):
    salt,pay_pin = hash_with_salt(pay_pin)
    for currency in Currencies:
        Balance.objects.create(amount=100,
                                pay_pin=pay_pin,
                                salt=salt,
                                currency_type = currency,
                                owner = owner,
                                )

    

def validate_form(req,form_type):
    if req.method == "POST":

        form = form_type(req.POST)

        if form.is_valid():
            return form,True

    else:
        form = form_type()
    
    return form,False

# make_qr('42',"USD")

