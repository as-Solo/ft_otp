#  Realizado por Solo a 13/08/2022 última actualización 13/08/2022 WIP.
# ------------------------------ LIBRERIAS -----------------------------------

import argparse
from cryptography.fernet import Fernet
import time
from Crypto.Hash import SHA256
from os import system
from code import save_key
from code import generate_totp

# ----------------------------- CONFIGURACION --------------------------------

parser = argparse.ArgumentParser(description='Generador de claves temporales')
grupo = parser.add_mutually_exclusive_group()

grupo.add_argument('-g', help = "Archiva tu clave maestra para futuros usos", type = str)
grupo.add_argument('-p', help = "Genera tu hash mediante un 'passphrase'", type = str)
parser.add_argument('-k', help = "Genera una clave temporal de un solo uso", action = 'store_true')

args = parser.parse_args()

# -------------------------------- EJECUCION ----------------------------------

if (args.g):
    if (save_key.inicializar(args.g)):
        save_key.guardar_key(args.g)

if (args.p):
    save_key.passphrase(args.p)

if (args.k):

    try:
        passw = generate_totp.recuperar_key()
        print (passw)
        totp = generate_totp.generar_totp(passw)
        print (f"\nTu clave para los proximos 30 segundos es {totp}")

    except:
        print ("Necesitas aportar una clave antes de generar tu contraseña temporal")
    
    

    

    