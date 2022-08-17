import tkinter
from code import save_key
from code import generate_totp

def pulsa(nombre):
    if passphrase.get() == '':
        resultado["text"] = "Debes intropducir una clave"
    else:
        save_key.passphrase(passphrase.get())
        resultado["text"] = passphrase.get()

def pulsa2():
    try:
        passw = generate_totp.recuperar_key()
        totp = generate_totp.generar_totp(passw)
        resultado2["text"] = (f"Tu clave para los proximos 30 segundos es")
        resultado3["text"] = f"{totp}"

    except:
        resultado3["text"] = "Necesitas aportar una clave antes de generar tu contraseña temporal"

ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title("GENERADOR TOTP")

etiqueta =tkinter.Label(ventana, text = "INTRODUCE UNA CONTRASEÑA", bg = "#aaaaaa")
etiqueta.pack(fill = tkinter.X)

passphrase = tkinter.Entry(ventana)
passphrase.pack()

boton = tkinter.Button(ventana, text = "generar hash", padx = 5, pady = 1, command = lambda : pulsa(passphrase))
boton.pack()

resultado = tkinter.Label(ventana)
resultado.pack()

etiqueta2 =tkinter.Label(ventana, text = "GENERAR TOTP", bg = "#aaaaaa")
etiqueta2.pack(fill = tkinter.X)

boton2 = tkinter.Button(ventana, text = "shut up and take my money", padx = 5, pady = 1, command = lambda : pulsa2())
boton2.pack()

resultado2 = tkinter.Label(ventana)
resultado2.pack()

resultado3 = tkinter.Label(ventana)
resultado3.pack()

ventana.mainloop()