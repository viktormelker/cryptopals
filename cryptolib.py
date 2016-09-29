import base64
from string import ascii_lowercase
from string import ascii_uppercase

# Performs bitwise Xor on 2 numbers 
def bitwiseXor(num1, num2):
    return num1 ^ num2

# performs base64 encoding on a hexstring
def base64Encode( hexString ):
   return base64.b64encode(hexString)

# rates the likelyhood of the text being english
def rateTextString(xoredText):
    rateCount = 0
    for i in range (0, 255):
        charsFound = xoredText.count(chr(i))
        if ((charsFound > 0) and (chr(i) in ascii_lowercase) or (chr(i) in ascii_uppercase)):
            rateCount = rateCount + charsFound
    return rateCount/len(xoredText)



