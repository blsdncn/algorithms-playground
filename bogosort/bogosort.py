import random
unsorted = [7,5,1,3,4,8,9,2,6]

def is_sorted(arr):
    for i in range(len(unsorted)-1):
        if(arr[i+1]<arr[i]):
            return False
    return True 

def bogoSort(arr):
    i = 0
    while not is_sorted(arr):
       i+=1
       print(f"Iterations: {i}",end='\r',flush=True)
       random.shuffle(arr)
    print(f"Total Iterations: {i}")
    return arr

sorted_array = bogoSort(unsorted)
print(sorted_array)