import pdb
import base64
import math
from string import ascii_lowercase
from string import ascii_uppercase
from collections import Counter
import matplotlib.pyplot as plt

# Performs bitwise Xor on 2 numbers of equal lengths
def bitwise_xor(num1, num2):
    return num1 ^ num2

# Performs bitwise Xor on a string using a single byte on every byte of the number.
# It returns the resulting string.
def bitwise_xor_single_byte(text, byte):
    arr = bytearray(text);
    #pdb.set_trace()
    for i in range(len(arr)):
        arr[i] = bitwise_xor(arr[i], byte)
    return str(arr)

# performs base64 encoding on a hex_string
def base_64_encode( hex_string ):
   return base64.b64encode(hex_string)

# rates the likelyhood of the text being english
def rate_text_string(text):
    common_chars = "ETAOINSRHetaoinsrh"
    less_common_chars = "DLUCMFYWGPBVKdlucmfywgpbvk"
    uncommon_chars = "XQJZxqjz1234567890,.-;:_!#%&/()\\=?+[]{}~| *"
    vowel_chars = "EAOIUYeaoiyu"
    consonant_chars = "BCDFHJKLMNPGRSTVWXZbcdfghjklmnpqrstvwxz"
    expected_vowel_factor = 0.41 # from https://en.wikipedia.org/wiki/Letter_frequency
    expected_word_frequency = 0.2 # approx 5 letter words on average
    
    common_chars_score = 10
    less_common_chars_score = 5
    uncommon_chars_score = 1
    other_chars_score = 0

    rate_count = 0
    num_vowel = 0
    num_consonant = 0
    chars_hit = []
    #pdb.set_trace()
    
    for i in range (0, 255):
        chars_found = text.count(chr(i))
        chars_hit.append(chars_found)

        if (chars_found > 0):
            if (chr(i) in common_chars):
                rate_count = rate_count + common_chars_score * chars_found
            elif (chr(i) in less_common_chars):
                rate_count = rate_count + less_common_chars_score * chars_found
            elif (chr(i) in uncommon_chars):
                rate_count = rate_count + uncommon_chars_score * chars_found
            else:
                rate_count = rate_count - other_chars_score * chars_found

            if chr(i) in vowel_chars:
                num_vowel = num_vowel + chars_found
            elif chr(i) in consonant_chars:
                num_consonant = num_consonant + chars_found;

    if (num_vowel+num_consonant) > 0:
        vowel_factor = num_vowel/float(num_vowel+num_consonant)
    else:
        vowel_factor = 0

    vowel_cons_discrepancy_factor = rate_frequency(vowel_factor, expected_vowel_factor, 0.5, 1)
    space_frequency = chars_hit[ord(' ')]/float(len(text))
    word_frequency_factor = rate_frequency(space_frequency, expected_word_frequency, 0.8, 1)

    return rate_count/float(len(text)) * vowel_cons_discrepancy_factor * word_frequency_factor

# try bitwise xor with a single byte. The byte is varied from 0 to 255.
# The min_rating is the minimum rating (returned from rate_text_string)
#   that is printed as a result.
# If print_all is true (non-zero?), then all texts with a higher rating then 
# min_rating are printed, otherwise only the best one is printed
def try_all_xor_bytes(text, min_rating, print_all):
    best_rating = -100
    best_byte = 0
    for num in range (0, 255):
        xored_ascii = bitwise_xor_single_byte(text, num)
        rate = rate_text_string(xored_ascii)
        #result_dict[num] = [xored_ascii, rate] 

        if ((print_all) and (rate > min_rating)):
            print ("Result Xored with %d got rating %f" % (num, rate)) 
            print ("xored_ascii was '%s'") % (xored_ascii)           

        if (rate > best_rating):
            best_rating = rate
            best_byte = num

    if (best_rating > min_rating):
        best_text = bitwise_xor_single_byte(text, best_byte)
        print("Best rating for bitwise xor was %f with byte %d" % (best_rating, best_byte)) 
        print("Decryption was '%s'" % (best_text))
    else:
        print("No bitwise xor decryption was good enough :(")
    return best_byte;

# scores the found frequency with a score. The scoring is based on a triangular
# distribution around the expected frequency where the score is equal to 
# score weight. The score goes to zero at expected_frequency * (1 + error_factor)
# and expected_frequency * (1 - error_factor)
#
# found_frequency is the frequency to be scored
# expected_frequency is the expected frequency
# error_factor is how much we expect that the frequency can differ 
# score_weight is how much the score can be max
def rate_frequency(found_frequency, expected_frequency, error_factor, score_weight):
   max_freq_diff = expected_frequency * error_factor 
   freq_diff = abs(found_frequency - expected_frequency)
   return max(0, score_weight * (1-freq_diff/float(max_freq_diff)))

# This function uses a key to encrypt a text using repeating xor
def xor_with_repeated_key(str_text, str_key):
    k = 0
    text_arr = bytearray(str_text)
    key_arr = bytearray(str_key)
    encrypted_arr = bytearray(str_text)
    key_length = len(str_key)
    pdb.set_trace()
    for i in range(len(text_arr)):
        encrypted_arr[i] = bitwise_xor(text_arr[i], key_arr[k])
        k = (k + 1) % key_length

    return str(encrypted_arr).encode("hex")

#
def get_hamming_distance(str1, str2):
    text_arr1 = bytearray(str1)
    text_arr2 = bytearray(str2)
    res = 0;

    for i in range(len(text_arr1)):
        hamming_byte = bitwise_xor(text_arr1[i], text_arr2[i])
        res = res + bin(hamming_byte).count("1")
    return res


def get_entropy(data, size):
    '''Calculate the entropy of the data represented by the counts list'''
    ent = 0.0
    for b in data:
        if b == 0:
            continue
        p = float(b)/size
        ent -= p*math.log(p, 256)
    return ent*8

def histogram(counts, sz, name):
    '''Use matplotlib to create a histogram from the data'''
    xdata = [n for n in xrange(0, 256)]
    data = [100*c/sz for c in counts]
    top = math.ceil(max(data)*10.0)/10.0
    rnd = [1.0/256*100]*256
    fig = plt.figure(None, (7, 4), 100)
    plt.axis([0, 255, 0, top])
    plt.xlabel('byte value')
    plt.ylabel('occurance [%]')
    plt.plot(xdata, data, label=name)
    plt.plot(xdata, rnd, label='continuous uniform')
    #plt.legend(loc=(0.49, 0.15))
    plt.savefig('hist-' + name+'.png', bbox_inches='tight')
    plt.close()
