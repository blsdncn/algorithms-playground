def binary_search(arr,target):
    n=len(arr)
    def helper(low,high):
        if low > high:
            return -1
        
        mid = (low+high)//2
        if(arr[mid]==x):
            return mid
        elif mid_val < target:
            return helper(mid+1,high)
        else:
            return helper(low,mid-1)
    return helper(0,n-1)
        