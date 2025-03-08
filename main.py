from binascii import unhexlify, hexlify
from Crypto.Cipher import AES

from test import *
from aes_modified import *
from analysys import *

aes_cipher = AES.new(key, AES.MODE_ECB)
aes_plaintexts = (plaintext_1, plaintext_2, plaintext_3, plaintext_4)

print("Key: \t\t\t\t", key_hex)
print()
for i in range(4):
    print(f"Test {i + 1}:")
    standard_AES = aes_cipher.encrypt(aes_plaintexts[i])
    modified_AES = aes(aes_plaintexts[i], key)
    print("AES128:\t\t\t\t", end=" ")
    print_cipher_text(standard_AES)
    print("AES modified KeyExpnasion:\t", end=" ")
    print_cipher_text(modified_AES)

    changed_plaintext = bytearray(aes_plaintexts[i])
    change_bit(changed_plaintext, 0, 5)

    changed_standard_AES = aes_cipher.encrypt(changed_plaintext)
    changed_modified_AES = aes(changed_plaintext, key)

    avalanche_effect_percentage(standard_AES, changed_standard_AES)
    avalanche_effect_percentage(modified_AES, changed_modified_AES)

    print()
