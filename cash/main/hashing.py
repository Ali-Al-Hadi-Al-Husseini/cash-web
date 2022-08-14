from .constants import  alphabet
from hashlib import sha256  
from random import choice


def hash(txt):
    return sha256(txt).hexdigest()

def get_salt():
    salt = []
    for _ in range(32):
        salt.append(choice(alphabet))
    return ''.join(salt)

def hash_with_salt(txt,salt=None):
    salt = get_salt() if salt == None else salt
 
    return salt,hash((str(txt)+salt).encode())