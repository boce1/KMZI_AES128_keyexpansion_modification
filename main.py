from binascii import unhexlify, hexlify
from Crypto.Cipher import AES

from test import *
from aes_modified import *
from analysys import *

def calculate_avalanche(bytearray):
    # changing every bit, and calculating the average
    temp = bytearray[:]
    sum_standard_aes = 0
    sum_modified_aes = 0
    for i in range(len(temp)):
        for j in range(8):
            change_bit(temp, i, j)
            changed_standard_AES = aes_cipher.encrypt(temp)
            changed_modified_AES = aes(temp, key)

            sum_standard_aes += avalanche_effect_percentage(standard_AES, changed_standard_AES)
            sum_modified_aes += avalanche_effect_percentage(modified_AES, changed_modified_AES)
            temp = bytearray[:]
            
    return sum_standard_aes / (len(temp) * 8), sum_modified_aes / (len(temp) * 8)


aes_cipher = AES.new(key, AES.MODE_ECB)
aes_plaintexts = (plaintext_1, plaintext_2, plaintext_3, plaintext_4)

# Printing results
print("Key: \t\t\t\t", key_hex)
print()
for i in range(4):
    print(f"Test {i + 1}:")
    standard_AES = aes_cipher.encrypt(aes_plaintexts[i])
    modified_AES = aes(aes_plaintexts[i], key)
    print("Plaintext:\t\t\t", end=" ")
    print_cipher_text(aes_plaintexts[i])
    print("AES128:\t\t\t\t", end=" ")
    print_cipher_text(standard_AES)
    print("AES modified KeyExpnasion:\t", end=" ")
    print_cipher_text(modified_AES)

    changed_plaintext = bytearray(aes_plaintexts[i])
    standard_aes_per, modified_aes_per = calculate_avalanche(changed_plaintext)
    print("Avalanche effect")
    print(f"Original: {standard_aes_per:.2f}%\t\t", end=" ")
    print(f"Modified: {modified_aes_per:.2f}%")
    print()
# # #