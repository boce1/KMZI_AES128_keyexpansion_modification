from binascii import unhexlify, hexlify
from Crypto.Cipher import AES

import test
from aes_modified import *

aes_cipher = AES.new(test.key, AES.MODE_ECB)

print("Test 1:")
ciphertext_1 = aes_cipher.encrypt(test.plaintext_1)
aes(test.plaintext_1, test.key)
#test.print_cipher_text(ciphertext_1)
print()
'''
print("Test 2:")
ciphertext_2 = aes_cipher.encrypt(test.plaintext_2)
test.print_cipher_text(ciphertext_2)
print()

print("Test 3:")
ciphertext_3 = aes_cipher.encrypt(test.plaintext_3)
test.print_cipher_text(ciphertext_3)
print()

print("Test 4:")
ciphertext_4 = aes_cipher.encrypt(test.plaintext_4)
test.print_cipher_text(ciphertext_4)
print()
'''
#key_expansion(test.key)
#keys = key_expansion(test.key)
#
#print(keys)
#for row in keys:
#    print(list(map(hex, row)))
