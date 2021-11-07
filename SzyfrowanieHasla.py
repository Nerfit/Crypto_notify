from cryptography.fernet import Fernet
import os

def encrypt(message: bytes, key: bytes) -> bytes:
    """
    Function used to encrypt email password before putting it in 'Settings.txt' file
    :param message: message to encrypt
    :param key: key used for encryption
    :return: Encrypted message
    """
    return Fernet(key).encrypt(message)
key = 'Hc2rxZW5uRJrvOLi5SjzEUxyxH3miRfH-6HieUjI_24='

msg = input('Podaj hasło do zaszyfrowania:\n')
token = encrypt(msg.encode(), key)
print('Wpisz poniższe hasło do pliku Settings.txt\n')
print(token.decode('utf-8'))

os.system("pause")


