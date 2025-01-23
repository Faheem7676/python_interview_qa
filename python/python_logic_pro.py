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




