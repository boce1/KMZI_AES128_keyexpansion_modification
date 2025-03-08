# Key and test bytes are NTFS test vectors

from binascii import unhexlify, hexlify

# hexademical representation of testing vectors
key_hex = "2b7e151628aed2a6abf7158809cf4f3c"
plaintext_1_hex = "6bc1bee22e409f96e93d7e117393172a"
plaintext_2_hex = "ae2d8a571e03ac9c9eb76fac45af8e51"
plaintext_3_hex = "30c81c46a35ce411e5fbc1191a0a52ef"
plaintext_4_hex = "f69f2445df4f9b17ad2b417be66c3710"
# # #

# raw bytes
key = unhexlify(key_hex)
plaintext_1 = unhexlify(plaintext_1_hex)
plaintext_2 = unhexlify(plaintext_2_hex)
plaintext_3 = unhexlify(plaintext_3_hex)
plaintext_4 = unhexlify(plaintext_4_hex)
# # #

def print_cipher_text(cipher_raw_bytes):
    print(hexlify(cipher_raw_bytes).decode())