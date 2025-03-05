# the volum of sphare is given as
def vol(rad):
    
    return (4/3)*(3.14)*(rad**3)

print(vol(2))


# write a function the check wether a number is in a given range (inclusive of high and log)
for item in range(0,5):
    
    print(item)
    
    
5 in range(0,10)


def ran_check(num,low,high):
    
   if  num in range(low,high+1):
       print(f"{num} is in range of {low} and {high}")
   else:
       print("not in range")    
       
print(ran_check(5,2,7))


def up_low(s):
    
    lowercase=0
    uppercase=0
    
    
    for char in s:
        if char.isupper():
            uppercase+=1
        elif char.islower():
            lowercase+=1
            
        else:
            pass    
        
    print(f"original string:",{s})
    print(f"Lowercase count:",{lowercase})
    print(f"Uppercase count:")
    
s="Hello Mr Roger , How are you this fin Tuesday"

print(up_low(s))


# write a python funtion that takes a list and returns a new list with unique elements of the first list
sample_list=[1,1,1,1,2,2,3,3,3,3,4,5]
#output Unique_list=[1,2,3,4,5]

def unique_list(lst):
    
    seen_number=[]

    for num in lst:
        if num not in seen_number:
            seen_number.append(num)
            
    return seen_number

# Write a python function to multiply all the numbers in a list
# sample_list=[1,2,3,-4]
# expected_list=[-24]

def multiply(numbers):
    
    total=1
    for num in numbers:
        total=total * num
        
    return total

print(multiply([1,2,3,-4,12]))



def palindrom(s):
    
    # Remove spaces string
    s=s.replace(" ","")
    
    # check is string==reverse version of the string
    
    
    return s==s[::-1]
print(palindrom("nurses run"))
print(palindrom("madam"))
print(palindrom("Malyalam"))

import string

def ispangram(str1,alphabet=string.ascii_lowercase):
    
        # create a set of alphabate 
        alphaset=set(alphabet)
        print(alphaset)
        
        # Remove any space from the input string
        str1=str1.replace(" ","")
        
        # Convert into all lowercase
        str1=str1.lower()
        print(str1)
        
        # Grab all unique letters from the strings
        str1=set(str1)
        print(str1)
        
        # alphabate set==string set input
        return str1==alphaset
    
        
print(ispangram("The quick brown  fox jumps over the lazy dog"))
    
    

