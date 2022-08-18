#  Realizado por Solo a 17/08/2022 última actualización 17/08/2022 WIP.

from cryptography.fernet import Fernet
from code import save_key

cryp = b'UZzuZlde6wZazH8_4pTQPxp952U31hiPtdv7Wms4vX0='
f = Fernet(cryp)

def format_data(word):
    if ':' in word:
        word.replace(':', '_')
        word.replace(' ', '')

def save_usr_pass(user, password):
    user = format_data(user)
    password = format_data(password)
    with open("data/ft_otp.key", "ab") as file:
        file.write(f"{f.encrypt(user)}:{f.encrypt(save_key.passphrase(password))}:{password}")

def get_user_data(user):
    data = []
    with open("data/ft_otp.key", "rb") as file:
        for linea in file:
            if (user + ' :') in f.decrypt(linea[:(len(user) + 2)]):
                data = f.decrypt(linea).split(':')
                return data
            else:
                print ("No se han encontrado registros con ese nombre de usuario.")


'''
def passphrase(key):
    m = SHA256.new()
    m.update(key.encode())
    user_hash = m.digest().hex()
    return user_hash

def format_data(word):
    if ':' in word:
        word.replace(':', '_')
        word.replace(' ', '')
    return word

def save_usr_pass(user, password):
    user = format_data(user)
    password = format_data(password)
    mensaje = f"{user}:{passphrase(password)}:{password}"
    print (mensaje)
    with open("../data/prueba.key", "r") as file:
        for linea in file:
            linea = f.decrypt(linea.encode()).decode()
            if (user + ':') in linea[:(len(user) + 1)]:
                print ("Ya te encuentras registrado, puedes generar claves temporales sin problema.")
                return 0
    with open("../data/prueba.key", "a") as file:
        file.write(f"{f.encrypt(mensaje.encode()).decode()}\n")
         

def get_user_data(user):
    data = []
    with open("../data/prueba.key", "r") as file:
        #mensaje = file.read()
        #desencriptado = f.decrypt(mensaje.encode()).decode()
        #print (desencriptado)
        #print (type(desencriptado))
        for linea in file:
            linea = f.decrypt(linea.encode()).decode()
            if (user + ':') in linea[:(len(user) + 1)]:
                data = linea.split(':')
                return data[1]
        print ("No se han encontrado registros con ese nombre de usuario.")

'''