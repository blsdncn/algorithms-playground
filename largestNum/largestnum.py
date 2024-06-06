#Find the largest number using a divide-and-conquer strategy.
def findLargestElement2(arr):
    if len(arr) == 0:
        return None
    return findLargest2(0,len(arr)-1,arr)

def findLargest2(i,j,arr):
    if i == j:
        return arr[i]
    mid = (i + j) // 2
    left = findLargest2(i,mid,arr)
    right = findLargest2(mid+1,j,arr)
    if left < right: return right
    else: return left

def findSmallestElement3(arr):
    if len(arr) == 0:
        return None
    return findSmallest3(0,len(arr)-1,arr)

def findSmallest3(i,j,arr):
    if i == j:
        return arr[i]
    if j == i + 1:
        return min(arr[i], arr[j])
    if j == i + 2:
        return min(arr[i], arr[i + 1], arr[i + 2])    
    mid = (j-i) // 3
    left = findSmallest3(i,mid,arr)
    center = findSmallest3(i+mid,i+2*mid,arr)
    right = findSmallest3(i+2*mid+1,j,arr)
    return min([left,center,right])



arr1 = []
arr2 = [1,2,3,4,5,6]
arr3 = [1,1,1,1,1]
arr4 = [9,2,7,2,9]
print(findSmallestElement3(arr1))
print(findSmallestElement3(arr2))
print(findSmallestElement3(arr3))
print(findSmallestElement3(arr4))