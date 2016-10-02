import sys 
import os
import pdb
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    i = 1
    #pdb.set_trace()
    cryptofile = open("cryptotexts.txt", "r")
    lines = cryptofile.readlines()
    for line in lines:
        print("Trying to decrypt line %d" % (i))
        normal_text = line[:-2].decode("hex")
        cryptolib.try_all_xor_bytes(normal_text, 2, 1)
        i = i + 1

    cryptofile.close()

if __name__ == "__main__":
    main()

# line 171 is encrypted.