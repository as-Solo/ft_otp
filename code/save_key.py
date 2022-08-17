#  Realizado por Solo a 13/08/2022 última actualización 17/08/2022 WIP.
# --------------------------- LIBRERIAS -------------------------------

from cryptography.fernet import Fernet
from Crypto.Hash import SHA256
from os import system

# ------------------------- CONFIGURACION -----------------------------

cryp = b'UZzuZlde6wZazH8_4pTQPxp952U31hiPtdv7Wms4vX0='
f = Fernet(cryp)

# --------------------------- FUNCIONES -------------------------------


def passphrase(key):
    m = SHA256.new()
    m.update(key.encode())
    user_hash = m.digest().hex()
    with open ("data/ft_otp.key", "wb") as file:
        file.write (f.encrypt(user_hash.encode()))

def inicializar(key):
    if len(key) >= 64:
        try:
            clave = bytes.fromhex(key)
            return True
        except:
            print ("La clave introducida no es un hexadecimal valido")
    else:
        print ("Faltan valores en tu clave")

def guardar_key(key):
    with open ("data/ft_otp.key", "wb") as file:
        file.write (f.encrypt(key.encode()))