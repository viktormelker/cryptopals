import sys 
import os
import pdb
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    #pdb.set_trace()
    orig_text = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = 'ICE'
    encrypted_text = cryptolib.xor_with_repeated_key(orig_text, key)
    print ("The encrypted text is %s" % (encrypted_text))
	

    

if __name__ == "__main__":
    main()