import base64

def main():
    hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    hex_data = hexString.decode("hex")
    b64String = base64Encode(hex_data)
    print (b64String)

def base64Encode( hexString ):
   return base64.b64encode(hexString)

if __name__ == "__main__":
    main()
