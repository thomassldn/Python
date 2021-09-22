#Collatz Conjecture, 3X + 1
#Author: Thomas S
#Date: 22 Sept 2021

#CollatzConjecture, takes a number and returns a list up to lenght provided
def collatzConjecture(num, length):
    currValue = 0
    collatzList = []
    while currValue < length:
        currValue += 1
        if isEven(num):
            num = num / 2
            collatzList.append(num)
        else:
            num = num * 3 + 1
            collatzList.append(num)
    return collatzList

def isEven( num):

    if num % 2 == 0:
        return True
    else:
        return False


print("Collatz Conjecture: ", collatzConjecture(332333, 200))
