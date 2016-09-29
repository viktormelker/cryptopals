import sys 
import os
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    hexString1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    hex_data1 = int(hexString1, 16) 

    for num in range (0, 255):
        xoredNum = cryptolib.bitwiseXor(hex_data1, num)
        xoredText = "%d" % (xoredNum)
        print ("xoredText was '%s'") %(xoredText)
        rate = cryptolib.rateTextString(hexString1)
        print ("Result Xored with %d got rating %f" % (num, rate))
    

if __name__ == "__main__":
    main()
