import sys 
import os
import pdb
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    normal_string = hex_string.decode("hex")
    #pdb.set_trace()
    for num in range (0, 255):
        xored_ascii = cryptolib.bitwise_xor_single_byte(normal_string, num)      

        rate = cryptolib.rate_text_string(xored_ascii)
        print ("Result Xored with %d got rating %f" % (num, rate))
        if (rate > 0.5):
            print ("xored_ascii was '%s'") % (xored_ascii)  
    

if __name__ == "__main__":
    main()
