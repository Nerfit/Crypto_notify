# import base64

settings_file = open('Settings.txt','r')
lines=[]
for line in settings_file:
    if not line.strip().startswith('#') and line.strip('\n').strip() != '':
        lines.append(line.strip('\n').strip())
settings_file.close()

print(lines)



# coded_string = 'RHppYXJtYWczMA=='
# decoded = base64.b64decode(coded_string)
# decoded = decoded.decode('utf-8')

# print(decoded)


# from cryptography.fernet import Fernet


# def decrypt(token: bytes, key: bytes) -> bytes:
#     return Fernet(key).decrypt(token)

# key = 'Hc2rxZW5uRJrvOLi5SjzEUxyxH3miRfH-6HieUjI_24='
# # print(key.decode())

# msg = input('Podaj hasło do zaszyfrowania:')
# token = encrypt(msg.encode(), key)
# print('Wpisz poniższe hasło do pliku Settings.txt\n')
# print(token)
# print(decrypt(token,key).decode())
# # print(pass)