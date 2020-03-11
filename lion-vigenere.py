import argparse
import string
import random






lines = """

A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

"""

lines = lines.strip()


character_array = lines.splitlines()

character_map = {}


for line in character_array:
    character_map[line[0].strip()] = (line.split("|")[1]).strip()



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
        
        pos = character_map[keys[index].upper()]
        loc = pos.split().index(v.upper())
        decoded += string.ascii_uppercase[loc]
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

            pos = character_map[keys[index].upper()]
        
            loc = string.ascii_uppercase.index(v.upper())
        
            encoded += pos.split()[loc]

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
# parser.add_argument("-f", dest='file', nargs=1, help="The path to file you want to write")
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
else: 
    if(args.keys):
        print("Encoding {} with the key {} ".format(args.values[0], args.keys[0]))
        keys = args.keys[0]
    else: 

        keys = get_random_key(values)
        print("Encoding {} with a random key {} ".format(values, keys))


args.opt(values,keys)

# print()