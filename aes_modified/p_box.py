def devide_bytes(word):
    byte1 = (word >> 24) & 0xFF
    byte2 = (word >> 16) & 0xFF
    byte3 = (word >> 8) & 0xFF
    byte4 = word & 0xFF

    return (byte1, byte2, byte3, byte4)

def p_box(word):
    byte1, byte2, byte3, byte4 = devide_bytes(word)

    output = (byte2 << 24) | (byte3 << 16) | (byte4 << 8) | byte1
    return output