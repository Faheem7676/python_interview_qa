# Write a function that takes in a list of integers and return True if it is contained 007
#in order

def spy_game(nums):
    
    code=[0,0,7,'x']
    #[0,7,'x]
    #[7,'x]
    #['x]
    
    for num in nums:
        
        if num ==code[0]:
            code.pop(0)
            
    return len(code)==1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# write a program that return the prime number that exist up to and including a given number
# By convention we will treat 0 and 1 as not prime

#map() #filter and lambda

def square(num):
    
    return num **2


my_nums=[1,2,3,4,5]

for item in map(square,my_nums):
    
    print(item)
    
    
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2==0:
        
        return "Even"
    else:
        return mystring[0]
    
names=["Andy","Eve","Sally"]

print(list(map(splicer,names)))


def check_even(num):
    
    return num%2==0

mynums=[1,2,3,4,5,6]

print(filter(check_even,mynums))

print(list(filter(check_even,mynums)))

for n in filter(check_even,mynums):
    
    print(n)
    
print("****************************")   
def square(n):
    
    result=n**2
    
    return result

print(square(2))

print("***********************")

def square(n):
    
    return n**2
    
   

print(square(2))

def square(num): return num**2

print(square(3))


square=lambda num:num**2

print(square(5))


print(list(map(lambda num:num**2,my_nums)))

print(list(filter(lambda num:num%2==0,mynums)))

print(names)

