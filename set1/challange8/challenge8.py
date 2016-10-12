import sys 
import os
import pdb
sys.path.append(os.path.abspath("../../"))
import cryptolib
import base64

def main():
    pdb.set_trace()
    keysize = 16
    cryptofile = open("cryptotexts.txt", "r")
    lines = cryptofile.readlines()
    cryptofile.close()

    i = 1;

    for line in lines:
        encrypted_text = line.rstrip('\n').decode("hex")
        data = bytearray(encrypted_text)
        counts = [0]*256
        for b in data:
            counts[b] += 1

        if (max(counts) > 4):
            print("Max occurance of char in line %d is %d" % (i, max(counts)))

        amounts = [0]*160
        for a in counts:
            amounts[a] += 1

        if (amounts[0] > 145):
            print("number of zeros in line %d is %d" % (i, amounts[0]))

        entropy = cryptolib.get_entropy(data, len(encrypted_text))
        #print("Entropy of line %d is %f" % (i , entropy))
        #cryptolib.histogram(counts, float(len(data)), "hist %d" % i)
        i = i + 1

        



if __name__ == "__main__":
    main()
