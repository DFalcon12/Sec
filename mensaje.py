from cryptography.fernet import Fernet

clave = Fernet.generate_key()
f = Fernet(clave)
token = f.encrypt(b'mensaje ultra secreto del servicio militar de la nueva republica rusa, tenemos entendido que la mayoria del pais ha sido bombardeado por misiles')
print(clave)
print(token)