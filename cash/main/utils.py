from importlib.resources import path
import qrcode
from .crud_utils import *
from .constants import Currencies

def make_qr(owner,currency):
    data = owner + "_--_" + currency
    qr = qrcode.QRCode(version=1,
                       box_size=8,
                       border=5)

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()

    img.save("C:\\Users\\lilo\\Documents\\GitHub\\cash-web\\cash\\main\\static\\qrcode\\" + data + '.png')


def make_qrcodes(owner_id):

    for currency in Currencies:
        make_qr(str(owner_id), currency)


def create_balances(owner,pay_pin):

    for currency in Currencies:
        Balance.objects.create(amount=1_000_000,
                                pay_pin=pay_pin,
                                currency_type = currency,
                                owner = owner,
                                )

    make_qrcodes(owner)

def validate_form(req,form_type):
    if req.method == "POST":

        form = form_type(req.POST)

        if form.is_valid():
            return form,True

    else:
        form = form_type()
    
    return form,False

# make_qr('42',"USD")