# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain
import  math

arr = [16,1,4,3,2,10,12,1,5,6,15,1]

def binary_search(arr, start, end, value_to_find):
    if start == end:
        if(value_to_find > arr[end]):
            return end + 1
        return end

    if start > end:
        return end

    mid = math.floor( (end + start) / 2 )


    if value_to_find < arr[mid]:
        return binary_search(arr, start, mid -1, value_to_find)
    if value_to_find > arr[mid]:
        return binary_search(arr, mid + 1, end, value_to_find)
    return mid

for index, value in enumerate(arr):
    new_location = binary_search(arr, 0, index, value)

    j = index
    new_value = arr[index]
    while j > new_location:
        arr[j] = arr[j-1]
        j -= 1
    arr[new_location] = new_value

print(arr)




