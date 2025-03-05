def reverse_string(s:str):
    
    return s[::-1]

print(reverse_string("python"))


str1="I am Faheem"


splt=str1.split()
print(splt)

reverse_string=" ".join(reversed(splt))
print(reverse_string)


print(str1[::-1])

print(str1[:-1])



##############################################
def stringreverse(s:str):
    
    if not isinstance(s,str):
        
        raise ValueError("input must be string")
    
    
    return s[::-1]

try:
    print(stringreverse("python"))
    print(stringreverse(54))
except ValueError as e:
    print(e)
    
################################################

# Find the First Non-Repeated Character

string="swiss"

char_count={}

# # count each character
for char in string:
    
    char_count[char]=char_count.get(char,0)+1
    
# Find the first non-repeated character
first_non_repeated=None
for char in string:
    if char_count[char]==1:
        first_non_repeated=char
        break
    
print("first_non_repeated_char:",{first_non_repeated})

#################################################

str="I am a software tester"

reverString=" ".join(reversed(str.split()))
print(reverString)


#####################################################
from collections import Counter

str="abcdabcdeffghiabc"
charectorCount=Counter(str)
print(charectorCount)
###############################################

# output only repeated char
string="avcdaabbeecddaabkd"
from collections import Counter

charcount=Counter(string)

print(charcount)

# filter and display only repeated chars
repeated_char={char:charcount for char, charcount in charcount.items() if charcount>1}


print(repeated_char)

############################################

string="THISISFAHEEMTHISMFAHT"

char_counts={}

for char in string:
    
    if char in char_counts:
        
        char_counts[char]=char_counts[char]+1
        
    else:
        char_counts[char]=1
        
print(char_counts)

#############################################


    
    











