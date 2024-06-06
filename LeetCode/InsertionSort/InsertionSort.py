
unsorted_array = [7, 2, 6, 9, 0, 5, 3, 2, 1, 8, 6, 3, 1, 3]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j +1] = key
    return arr

sorted_array = insertion_sort(unsorted_array)
print(sorted_array)