/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *indices = (int*) malloc(2*sizeof(int)); //allocate an array of two integers to hold our resulting indices
    for(int i = 0; i < numsSize; i++){
        indices[0] = i; //assign the first index to the first unchecked digit in nums
        for(int j = i+1; j < numsSize; j++){ //iterate through each combination of the nums[i] and remaining unchecked values of nums
            if(nums[i] + nums[j] == target){ //check if numbers at i and j add up to target
                indices[1] = j; // if the two numbers add up to target, assign the second index to j
                *returnSize=2;
                return indices; //return our allocated indices array
            }
        }
    }
    returnSize = 0;
    free(indices); // we free here because if no valid solution is found, then our indices array won't be returned, thus won't be freed by the caller.
    return NULL;
}

