# AES Key Expansion Modification and Avalanche effect with NTFS tests vectors

## Overview
This project involves modifications to the AES-128 key expansion process while maintaining the core encryption and decryption structure. The changes impact how round keys are generated. To validate the effectiveness of this modified AES, NTFS test vectors are used as input data.

## Key Expansion Modification

### Key Expansion Schema
Below is the updated key expansion methodology:

![Key Expansion Schema](key%20expansion%20schema.png)

### Modified Formula
A custom transformation function has been applied to the key schedule, differing from the original AES key expansion.

**![Modified Formula](modified%20formula.png)**

## Testing Methodology
- NTFS-based plaintext blocks are encrypted using the modified AES and standard AES.
- For every test only 1 bit is changed of the original plaintext.
- For every test program calculates percentage of changed bits in the cipher text.
- The final result is average of the all tests

