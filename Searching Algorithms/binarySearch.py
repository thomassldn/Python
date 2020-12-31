#Binary Search, recursive
#time complexity O(log n)
#best time O(1)

def binarySearch(arr, l, r, x ):
    #check if r >= l
    if r >= l :
      mid = l + (r - l) // 2
      #check if mid == x
      if arr[mid] == x:
        return mid
      #if arr[mid] is greater than x, search left side
      elif arr[mid] > x:
        return binarySearch(arr, l, mid - 1, x )

      else:
        return binarySearch(arr, mid + 1, r, x)
    else:
      return -1

#Execution begins
arr = [5,9,33,1,99,44,2,7]

print("Array before sorting:", arr)

x = 99

arr.sort()

print("Array after sorting: ", arr)

#call binarySearch, search for number
index = binarySearch(arr, 0, len(arr) - 1, x)

if index == -1:
  print("Value does not exist in array!")
else:
  print("Value exist at index: ", index)

#Output:
#Array before sorting: [5, 9, 33, 1, 99, 44, 2, 7]
#Array after sorting:  [1, 2, 5, 7, 9, 33, 44, 99]

#Value exist at index:  7



