import qrcode
from .crud_utils import *

def make_qr(email):
    data = email
    qr = qrcode.QRCode(version=1,
                       box_size=10,
                       border=5)

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='red',
                        back_color='black')

    img.save('shein.png')
    


def validate_form(req,form_type):
    if req.method == "POST":

        form = form_type(req.POST)
        if form.is_valid():
            return form,True

    else:
        form = form_type()
    
    return form,False