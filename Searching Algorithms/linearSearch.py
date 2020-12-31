#Linear Search
#time complexity O(n)

def linearSearch(arr, x):

    for index in range(len(arr)):
        if arr[index] == x:
            return index;

    return -1

#Execution Begins
arr = [2,66,7,9,1,0,99,45,57]

#value we are looking for
x = 45

index = linearSearch(arr, x)

if index == -1:
    print("Value is not present in set!")
else:
    print("Value exists at index: ", index)

#Output:
#Value exists at index:  7



