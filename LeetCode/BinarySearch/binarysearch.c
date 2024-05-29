int search(int* nums, int numsSize, int target) {
    int left= 0;
    int right = numsSize-1;
    while(left<=right){
        //calculates midpoint by offsetting left by half the distance between left and right
        int middle = left + (right - left) / 2; 
        if(nums[middle] == target){
            return middle;
        }
        if (nums[middle] < target) {
            left = middle + 1; // move left pointer beyond middle
        } else {
            right = middle - 1; // move right pointer before middle
        }
    }
    return -1;
}

searchRecursive(int* nums, int numsSize, int target){
    
}