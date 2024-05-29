int findPivot(int* nums, int numsSize) {
    int left = 0;
    int right = numsSize - 1;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (middle < right && nums[middle] > nums[middle + 1]) {
            return middle + 1;
        } else if (middle > left && nums[middle] < nums[middle - 1]) {
            return middle;
        }
        
        if (nums[middle] >= nums[right]) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }
    return 0;
}

int search(int* nums, int numsSize, int target) {
    int pivot = findPivot(nums, numsSize);
    int left = 0;
    int right = numsSize - 1;
    
    while (left <= right) {
        int middle = left + (right - left) / 2;
        int realMid = (middle + pivot) % numsSize;
        if (nums[realMid] == target) {
            return realMid;
        }
        if (nums[realMid] < target) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }
    return -1;
}




int main(){
    int numsSize = 7;
    int* nums[numsSize];
    nums[4];
    nums[5];
    nums[6];
    nums[7];
    nums[0];
    nums[1];
    nums[2];
    printf("Pivot: %d\n",findPivot(nums, numsSize));
}
    

