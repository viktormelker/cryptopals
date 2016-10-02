import sys 
import os
import pdb
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    normal_string = hex_string.decode("hex")
    pdb.set_trace()
    cryptolib.try_all_xor_bytes(normal_string, 1, 1)

    

if __name__ == "__main__":
    main()
