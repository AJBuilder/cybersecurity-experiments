# %%
import os
from Crypto.Cipher import AES
import binascii

dictFile = open("words.txt", "r")
dictionary = dictFile.read().splitlines()

plaintext = b"This is a top secret."
ciphertext = b"3f814d00c3f1047f1dfa879115970472472a17eabdd9ba4fcd667743e1e03674"

def pad(m):
    return bytes(m)+bytes([16-len(m)%16])*(16-len(m)%16)


# %%
dictIndex = 0
iv = b'\x00' * 16
paddedPlaintext = pad(plaintext)
print("Padded plaintext: " + str(paddedPlaintext))
print("Ciphertext:" + str(ciphertext))

for dictIndex in range(0, len(dictionary)):
    print()
    key = bytes(dictionary[dictIndex], 'utf-8') + b'\x20' * (16 - (len(dictionary[dictIndex]) % 16))
    print("Trying : " + str(dictionary[dictIndex]) + " \tPadded key: " + str(key))

    encoded = AES.new(key, AES.MODE_CBC, iv).encrypt(paddedPlaintext)
    print("Encoded: " + str(binascii.hexlify(encoded)) + " with key " + str(binascii.hexlify(key)))
    if str(binascii.hexlify(encoded)) == str(ciphertext):
        print("Found key! -> " + str(dictionary[dictIndex]))
        break


