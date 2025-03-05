print([1,2,3,4,5])
print([6,7,8,9,10])
print([11,12,13,14,15])


def display(row1,row2,row3):
    
    print(row1)
    print(row2)
    print(row3)
    
example_row=[1,2,3]
display(example_row,example_row,example_row)


def display(row1,row2,row3):
    
    print(row1)
    print(row2)
    print(row3)
    
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]

print(display(row1,row2,row3))

row2[1]="X"
print(display(row1,row2,row3))
