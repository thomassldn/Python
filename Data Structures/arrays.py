#Date: 18 Aug 2021
#Thomas S
#Arrays

#Import array module
from array import *

#Create and print array
print( "Create and print array\n","=========================")
arry = array('i', [29,2,5,67,6])


for i in arry:
    print(i)

#Insert element into the array
print( "\nInsert element 9 into the array\n","=========================")
arry.insert(2,9)

for i in arry:
    print(i)


#Remove element from the array
print( "\nRemove 29 from the array\n","=========================")

arry.remove(29)

for i in arry:
    print(i)

#Search index of element
print( "\nSearch index of element\n","=========================")

location = arry.index(67)

print(location)
