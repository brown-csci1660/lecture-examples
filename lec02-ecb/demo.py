from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
import sys
import ast
import os

def getPPM(file):

    image = Image.open(file)
    # convert to bitmap
    image.save("tmp.ppm", format="PPM")
    # parse ppm
    with open("tmp.ppm", "rb") as ppm:
        i = 0
        head = []
        tail = []
        for line in ppm:
            if i < 3:
                head.append(line)
            else:
                tail.append(line)
            i += 1


    tail = b''.join(tail)

    return head, tail

def symmetric_encrypt(plaintext, key, mode):
    print("Using key: " + str(key))
    padder = sym_padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext)
    padded_data += padder.finalize()
    if mode == "ECB":
        mode = modes.ECB()
    if mode == "CBC":
        mode = modes.CBC(os.urandom(16))
    cipher = Cipher(algorithms.AES(key), mode)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext



def write_out(head, tail_cipher, mode):
    new_file = b''.join(head + [tail_cipher])

    # save bytes
    with open("tmp.ppm", "wb") as ppm:
        ppm.write(new_file)

    # convert to png
    out = Image.open(open("tmp.ppm",'rb'))
    out.show()
    out.save(f"output.{mode}.png")

    # clean up
    os.remove("tmp.ppm")




def fail():
    print("usage: python demo.py <image>.png <{CBC, ECB}> <(OPTIONAL) key in format: \"b\'\x00 ...\'\">")
    exit(1)


if __name__ == '__main__':

    if len(sys.argv) == 4:
        key = ast.literal_eval(sys.argv[3])

    elif len(sys.argv) == 3:
        key = os.urandom(32)

    else:
        fail()

    file = sys.argv[1]
    mode = sys.argv[2]
    if mode not in ["CBC", "ECB"]:
        fail()

    head, tail = getPPM(file)
    tail_cipher = symmetric_encrypt(tail, key, mode)
    write_out(head, tail_cipher, mode)
