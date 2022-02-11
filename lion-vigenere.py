import argparse
import string
import random
import re

def panic(values, keys):
  #  print(len(values.replace(" ", ""))== len(keys))
    return (len(values.replace(" ", "")) != len(keys)) or ((re.search(r"\W",keys)))

def print_it(words, keys, decoded=True):
    val = ""
    if(decoded):
        val+="Decoded: "
    else:
        val+= "Encoded: "

    val+= (words.lower() + "\n")

    val+=("Key: " + keys)

    print(val)
 
def decode(values, keys): 
    decoded = ""
    index = 0

    # decoded.upper()   
    for v in values: 
        if(v == " "):
            decoded+=" "
            continue
        
        pos = (string.ascii_lowercase.index(v.lower()) 
        - string.ascii_lowercase.index(keys[index].lower()))   % len(string.ascii_lowercase)
       
        decoded += string.ascii_uppercase[pos]
        index+=1

    print_it(decoded,keys)
    #return decoded.lower()

def encode(values, keys):
    encoded = ""
    index = 0

    for v in values:
        try:
            if(v == " "):
                encoded+=" "
                continue
        
            pos = (string.ascii_lowercase.index(v.lower()) 
             + string.ascii_lowercase.index(keys[index].lower()))   % len(string.ascii_lowercase)
       
            encoded += string.ascii_uppercase[pos]

            index += 1
        except KeyError:
            print("yeyy")
            break

    
    print_it(encoded, keys, False)
    
def get_random_key(values):
    length = len(values.replace(" ", ""))
    random_key = ""
    for i in range(length):
        random_key+= string.ascii_lowercase[random.randint(0, 25)]
    
    return random_key



parser = argparse.ArgumentParser(
    description = """ 
    Vigenere Cipher Decoding Utiliy \n
    Author: kosiken<allisonkosy@gmail.com> """, epilog="""
    example:
    $python lion-vignere.py abcd ztuw --file dest.txt"""
)

parser.add_argument("values",
help = "The text to decrypt or encrypt"
,type=str,
nargs=1,metavar='text'



)
parser.add_argument("-k",
help = "The key to use to decrypt or encrypt the text"
,type=str,
nargs=1,metavar='key',
dest="keys"



)



parser.add_argument("-e", dest="opt", const=encode, 
default=decode, help="Change mode to encrypt the text",action="store_const")
# parser.add_argument("--fil", dest='file', nargs=1, help="The path to file you want to write")
parser.add_argument("-f", dest='file', nargs=1, help="The path to file you want to write")
args = parser.parse_args()

# if(len(args.values[0])!= len(args.keys[0])): 
#     print("Error: The length of the key and text to decode  must be the same")
#     exit()
keys =""
values = ""

values = args.values[0]

if(args.opt == decode):
    if(args.keys == None):
        print("error you have to specify a key")
    print("Decoding {} with the key {} ".format(args.values[0], args.keys[0]))
    keys = args.keys[0]
    if(panic(values, keys)): 
        print("Error: The length of the key and text to decode  must be the same")
        exit()
else: 
    if(args.keys):
        print("Encoding {} with the key {} ".format(args.values[0], args.keys[0]))
        keys = args.keys[0]
    else: 

        keys = get_random_key(values)
        print("Encoding {} with a random key {} ".format(values, keys))
    
    if(panic(values, keys)): 
        print("Error: The length of the key and text to decode  must be the same \n and the key must not contain non alphabetical characters")
        exit()


args.opt(values,keys)

# print()
