import sys 
import os
import pdb
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    pdb.set_trace()
    text = "YELLOW SUBMARINE"
    data = bytearray(text)
    padChar = 0x04
    paddedData = cryptolib.padToLength(data, 20, padChar)
    print(paddedData);


if __name__ == "__main__":
    main()
