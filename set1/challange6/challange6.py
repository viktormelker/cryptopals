import sys 
import os
import pdb
sys.path.append(os.path.abspath("../../"))
import cryptolib

def main():
    pdb.set_trace()
    text1 = "this is a test"
    text2 = "wokka wokka!!!"
    hamming_distance = cryptolib.get_hamming_distance(text1, text2)
    #print ("hamming distance was %d" % (hamming_distance))

    cryptofile = open("cryptotexts.txt", "r")
    lines = cryptofile.readlines()
    encrypted_text = ""
    for line in lines:
        encrypted_text = encrypted_text + line

    guessed_keysize = get_estimated_keysize(encrypted_text)
    separate_texts = []
    best_texts = []
    for i in range(guessed_keysize):
        separate_texts.append("")
        best_texts.append("")

    for i in range(len(encrypted_text)):
        separate_texts[i % guessed_keysize] = separate_texts[i % guessed_keysize] + encrypted_text[i]

    for i in range(guessed_keysize):
        print("trying to solve block %d" %(i))
        best_byte = cryptolib.try_all_xor_bytes(separate_texts[i], 4, 0)
        best_texts[i] = cryptolib.bitwise_xor_single_byte(separate_texts[i], best_byte)

    final_text = ""
    for i in range(len(best_texts[0])-1):
        for j in range(guessed_keysize):
            final_text = final_text + best_texts[j][i]

    rating = cryptolib.rate_text_string(final_text)
    print("Decrypted text got rating %f and was '%s'" % (rating, final_text)) 



# this function guesses the keysize that was used to encrypt the text.
# the encrypted_text is assumed to have been encrypted with xor.
# the function uses the fact that the key repeats itself and leaves
# a periodic trace in the encrypted text with the same size as the
# keysize
def get_estimated_keysize(encrypted_text):
    min_keysize = 2
    max_keysize = 40
    min_dist = 1000
    best_keysize = 0
    num_avg_sections = 20
    for i in range(min_keysize, max_keysize + 1):
        ham_dist_per_byte = 0;
        first_part = encrypted_text[0: i]
        for j in range(2, num_avg_sections + 2):
            second_part = encrypted_text[i*(j-1): j*i]
            hamming_distance = cryptolib.get_hamming_distance(first_part, second_part)
            ham_dist_per_byte = ham_dist_per_byte + hamming_distance/float(i) 

        ham_dist_per_byte = ham_dist_per_byte /(num_avg_sections)
        print("hamming distance (normed) for keysize %d was %f" % (i, ham_dist_per_byte))
        if (ham_dist_per_byte < min_dist):
            min_dist = ham_dist_per_byte
            best_keysize = i 

    print("Smallest distance was %f with keysize %d" % (min_dist, best_keysize))
    return best_keysize
    
    

if __name__ == "__main__":
    main()