import os
from Enigma import Enigma

# so that we can just call them without needing to know where they actually are
os.chdir(os.path.dirname(__file__))


def encipher_string(seed: any, data: bytearray):
    e = Enigma(seed)
    encoded_buffer = bytearray()

    for b in data:
        encoded_byte = e.encipher(b)
        encoded_buffer.append(encoded_byte)

    return encoded_buffer


def encipher_file(infile_path: str, outfile_path: str, seed: any):
    # always remember to close the file so that you don't corrupt that file. However, because python closes the file automatically, we're safe
    # Open in and out files in binary format
    with open(infile_path, 'rb') as infd, open(outfile_path, 'wb') as outfd:
        # Infinite loop we break out of when no more data is read
        # Create enigma object
        e = Enigma(seed)
        while True:
            # Read in 64 bytes of data. This is usually a lot more
            buffer = infd.read(64)
            # If we are not at the end of the file
            if buffer:
                # Create a bytearray to store data
                enciphered_buffer = bytearray()

                # encipher each value
                for b in buffer:
                    encoded_byte = e.encipher(b)
                    enciphered_buffer.append(encoded_byte)
                outfd.write(enciphered_buffer)
            else:
                # buffer was a falsey value so no data read
                # we are at the end of the file
                break


def main():
    # s = "test"
    # data = bytearray(s.encode('UTF-8'))
    # ciphertext = encipher_string(100, data)
    # print(ciphertext)

    # plaintext = encipher_string(100, ciphertext)
    # plaintext = plaintext.decode('UTF-8')
    # print(plaintext)

    infile_path = "plaintext.txt"
    outfile_path = "ciphertext.txt"
    outfile2_path = "decoded.txt"
    seed = 25

    encipher_file(outfile_path, outfile2_path, seed)


if __name__ == "__main__":
    main()
