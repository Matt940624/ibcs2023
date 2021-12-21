# main.py
import os
from Enigma import Enigma

os.chdir(os.path.dirname(__file__))


def encipher(seed: any, data: bytearray):
    e = Enigma(seed)
    encoded_buffer = bytearray()

    for b in data:
        encoded_byte = e.encipher(b)
        encoded_buffer.append(encoded_byte)

    return encoded_buffer


def main():
    s = "your mom"
    data = bytearray(s.encode('UTF-8'))
    ciphertext = encipher(100, data)
    print(ciphertext)

    plaintext = encipher(100, ciphertext)
    print(plaintext)


if __name__ == '__main__':
    main()
