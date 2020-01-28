import sys
import hashlib

def encrypt(text,s):
    result = ""
    for i in text:
        result += chr((i + s) % 256)
    return result

def decrypt(text, s):
    result = ""
    for i in text:
        result += chr((ord(i) - s) % 256)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("No file name was provided")
    else:
        if sys.argv[1] == '-e':
            f = open(sys.argv[3], 'rb')
            c = hash(int(sys.argv[2]))
            e = encrypt(f.read(), c)
            fe = open("encrypted.txt", 'w', encoding='utf-8')
            fe.write(e)
            fe.close
        elif sys.argv[1] == '-d':
            f = open(sys.argv[3], 'r', encoding='utf-8')
            c = hash(int(sys.argv[2]))
            print(decrypt(f.read(), c))
        f.close
