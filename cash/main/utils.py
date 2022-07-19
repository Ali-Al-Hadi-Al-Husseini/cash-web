from importlib.resources import path
import qrcode
from .crud_utils import *


def make_qr(owner,currency):
    data = owner + "_--_" + currency
    qr = qrcode.QRCode(version=1,
                       box_size=10,
                       border=5)

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()

    img.save("C:\\Users\\lilo\\Documents\\GitHub\\cash-web\\cash\\main\\static\\qrcode\\"+ data + '.png')


def make_qrcodes(owner_id):
    make_qr(str(owner_id), "USD")
    make_qr(str(owner_id), "LB")

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
    make_qrcodes(owner.id)

def validate_form(req,form_type):
    if req.method == "POST":

        form = form_type(req.POST)

        if form.is_valid():
            return form,True

    else:
        form = form_type()
    
    return form,False

# make_qr('42',"USD")