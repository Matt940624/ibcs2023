# main.py
import os
from Enigma import Enigma

os.chdir(os.path.dirname(__file__))


def encipher_string(seed: any, data: bytearray):
    e = Enigma(seed)
    encoded_buffer = bytearray()

    for b in data:
        encoded_byte = e.encipher(b)
        encoded_buffer.append(encoded_byte)

    return encoded_buffer
def encipher_file(infile_path: str, outfile_path: str, seed: any):
#Open in and out files in binary format
    with open(infile_path, 'rb') as infd, open(outfile_path, 'wb') as outfd:
#   Infinite loop we break out of when no more dtat is read
        while True:
#         read in 64 bytes of data. This is usually a lot more 
           buffer = infd.read(64)
#            If we are not at the end of the file
        if buffer:
#         Create bytearray to store data
            enciphered_buffer = bytearray()
#     encipher each value
            for b in buffer:
                encoded_byte = e.encipher(b)
                enciphered_buffer.append(encoded_byte)
            outfd.write(enciphered_buffer)
         else: 
            break

def main():
    s = "your mom"
    data = bytearray(s.encode('UTF-8'))
    ciphertext = encipher(100, data)
    print(ciphertext)

    plaintext = encipher(100, ciphertext)
    print(plaintext)


if __name__ == '__main__':
    main()

jdksla;fjdklsajijla 
