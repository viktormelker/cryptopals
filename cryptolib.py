import pdb
import base64
from string import ascii_lowercase
from string import ascii_uppercase


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
def rate_text_string(xored_text):
    rate_count = 0
    chars_hit = [];
    #pdb.set_trace()
    for i in range (0, 255):
        chars_found = xored_text.count(chr(i))
        chars_hit.append(chars_found)
        if (chars_found > 0):
            if ((chr(i) in ascii_lowercase) or (chr(i) in ascii_uppercase)):
                rate_count = rate_count + chars_found
            else:
                rate_count = rate_count - chars_found
    return rate_count/float(len(xored_text))
