from binascii import unhexlify, hexlify
from Crypto.Cipher import AES

from test import *
from aes_modified import *

aes_cipher = AES.new(key, AES.MODE_ECB)
aes_plaintexts = (plaintext_1, plaintext_2, plaintext_3, plaintext_4)

for i in range(4):
    print(f"Test {i + 1}:")
    standard_AES = aes_cipher.encrypt(plaintext_1)
    modified_AES = aes(aes_plaintexts[i], key)
    print_cipher_text(standard_AES)
    print_cipher_text(modified_AES)
    print()
