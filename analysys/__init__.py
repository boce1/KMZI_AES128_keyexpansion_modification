# analysys of avalanche effect

def hamming_distance(bytes1, bytes2):
    # Count the number of differing bits between two byte arrays
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(bytes1, bytes2))

def avalanche_effect(bytes1, bytes2):
    return hamming_distance(bytes1, bytes2) / (len(bytes1) * 8) * 100

def change_bit(data, byte_index, bit_index):
    data[byte_index] ^= (1 << bit_index)