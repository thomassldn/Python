#Bubble Sort
#Thomas Saldana
#3 March 2019
#Avg Time Complexity: O(n^2), O(n) when array is sorted. 

def bubbleSort(arr):
    temp = 0;
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

#Execution Begins
arr = [5,1,89,3,9,3,33,42,7,99,100,34,78,95]

#Print array before sorting
print("Array before sorting: \n", arr)

#Sort the Array
bubbleSort(arr)

#Print array before sorting
print("Array after sorting: \n", arr)
