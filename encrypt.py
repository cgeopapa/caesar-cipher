import sys
import hashlib

def encrypt(text,s):
    result = ""
    for i in text:
        result += chr(ord(i) + s)
    return result

def decrypt(text, s):
    result = ""
    for i in text:
        result += chr(ord(i) - s)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("No file name was provided")
    else:
        f = open(sys.argv[3], 'r')
        if sys.argv[1] == '-e':
            c = hash(int(sys.argv[2])) % 256
            e = encrypt(f.read(), c)
            fe = open("encrypted.txt", 'w')
            fe.write(e)
            fe.close
        elif sys.argv[1] == '-d':
            c = hash(int(sys.argv[2])) % 256
            print(decrypt(f.read(), c))
        f.close
