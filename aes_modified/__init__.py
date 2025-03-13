from .s_box import *
from .p_box import *

# MODIFIED PART OF AES
def g(word):
    # word is 32bits or 4 bytes
    byte1, byte2, byte3, byte4 = devide_bytes(word)

    next_byte_1 = substitution(byte1)
    next_byte_4 = substitution(byte4)

    next_byte_2 = next_byte_1 ^ byte2
    next_byte_3 = byte3 ^ next_byte_4

    next_byte_2 = substitution(next_byte_2)
    next_byte_3 = substitution(next_byte_3)

    output = (next_byte_1 << 24) | (next_byte_2 << 16) | (next_byte_3 << 8) | next_byte_4
    output = p_box(output)
    return output
    

def key_expansion(key_raw_bytes):
    words = [int.from_bytes(key_raw_bytes[i:i+4], byteorder="big") for i in range(0, len(key_raw_bytes), len(key_raw_bytes) // 4)]

    keys_output = [] # array of ints
    key_row = []

    for i in range(11): # 1 key per round, there is 10 rounds + 1 key for initialializing block
        # round
        words[1] = g(words[1])
        words[2] = g(words[2])  

        words[0] ^= words[1]
        words[3] ^= words[2]

        for j in range(4):
            key_row.extend(devide_bytes(words[j]))
        keys_output.append(key_row)
        key_row = []
        # round
    #for i in range(11): # visualizing key expansion
    #    print(list(map(hex, keys_output[i])))
    return keys_output
# # #



# # # 
# AES standard
def sub_bytes(matrix):
    for i in range(len(matrix)):
        matrix[i] = substitution(matrix[i])


def shift_rows(matrix):
    matrix[:] = matrix[0:4] + \
                matrix[5:8] + [matrix[4]] + \
                matrix[10:12] + matrix[8:10] + \
                [matrix[15]] + matrix[12:15] 

def mix_columns(matrix):

    # Define the fixed matrix used in mix columns
    # [ 2 3 1 1 ]
    # [ 1 2 3 1 ]
    # [ 1 1 2 3 ]
    # [ 3 1 1 2 ]
    
    # Galois Field multiplication functions
    def gmul(a, b):
        """Multiply two numbers in the GF(2^8) field"""
        p = 0
        for i in range(8):
            if b & 1:
                p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            if hi_bit_set:
                a ^= 0x1B  # x^8 + x^4 + x^3 + x + 1
            b >>= 1
        return p & 0xFF  # Ensure result is 8 bits

    # Transformation functions
    def mul_by_2(a):
        return gmul(a, 2)
    
    def mul_by_3(a):
        return gmul(a, 3)
    
    # Process each column (4 columns)
    for col in range(4):
        # Get the column values
        c0 = matrix[col * 4]
        c1 = matrix[col * 4 + 1]
        c2 = matrix[col * 4 + 2]
        c3 = matrix[col * 4 + 3]
        
        # Calculate the new values
        matrix[col * 4] = mul_by_2(c0) ^ mul_by_3(c1) ^ c2 ^ c3
        matrix[col * 4 + 1] = c0 ^ mul_by_2(c1) ^ mul_by_3(c2) ^ c3
        matrix[col * 4 + 2] = c0 ^ c1 ^ mul_by_2(c2) ^ mul_by_3(c3)
        matrix[col * 4 + 3] = mul_by_3(c0) ^ c1 ^ c2 ^ mul_by_2(c3)

def add_round_key(matrix, round_key):
    for i in range(len(matrix)):
        matrix[i] ^= round_key[i]

def aes(plaintext_raw_bytes, key_raw_bytes):
    plaintext_int = [x for x in plaintext_raw_bytes]
    keys_int = key_expansion(key_raw_bytes)

    # preround
    add_round_key(plaintext_int, keys_int[0])
    # # #

    for i in range(1, 10): # 1 to 9 (9 rounds)
        round_key = keys_int[i]
        sub_bytes(plaintext_int)
        shift_rows(plaintext_int)
        mix_columns(plaintext_int)
        add_round_key(plaintext_int, round_key)

    # final round
    sub_bytes(plaintext_int)
    shift_rows(plaintext_int)
    add_round_key(plaintext_int, keys_int[len(keys_int) - 1])

    return bytearray(plaintext_int)

# # #