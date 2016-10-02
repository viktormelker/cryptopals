import sys 
import os
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    hex_string1 = '1c0111001f010100061a024b53535009181c'
    hex_string2 = '686974207468652062756c6c277320657965'
    hex_data1 = int(hex_string1, 16) 
    hex_data2 = int(hex_string2, 16) 
    print(hex_data1)
    print(hex_data2)
    res = cryptolib.bitwise_xor(hex_data1, hex_data2)
    print (hex(res))

if __name__ == "__main__":
    main()
