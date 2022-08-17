#  Realizado por Solo a 13/08/2022 última actualización 17/08/2022 WIP.
# --------------------------- LIBRERIAS -------------------------------

from cryptography.fernet import Fernet
import time
from Crypto.Hash import SHA256
from os import system

# -------------------------- CONFIGURACION ----------------------------

cryp = b'UZzuZlde6wZazH8_4pTQPxp952U31hiPtdv7Wms4vX0='
f = Fernet(cryp)

# --------------------------- FUNCIONES -------------------------------

def recuperar_key():
    with open ("data/ft_otp.key", "rb") as file:
            return f.decrypt(file.read()).decode()

def generar_totp(key):
    barra = int(time.time()%30)
    while (int(time.time()%30) != 0):
        system (f"echo -n \r\033k[{'#' * (int(time.time()%30) - barra)}{'-' * (29 - int(time.time()%30))}]   {100 * int(time.time()%30) // 29}% Generando tu clave")
        time.sleep(1)
    key = key + str(int(time.time()/30))
    m = SHA256.new()
    m.update(key.encode())
    hexa_raw = m.digest()
    numero = (hexa_raw.hex()[4:10])
    totp = str(int(numero, 16))[:6]
    if len(totp) < 6:
            for i in range (6 - len(totp)):
                totp = '0' + totp
    return totp