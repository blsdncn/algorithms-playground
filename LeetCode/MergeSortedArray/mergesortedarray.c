void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    // Get ((m+n)-1)th index, decrement to set m and n to the index of the last value of nums1 and nums2 respectively.
    int ptr = (n--) + (m--) - 1;
    // Iterate through length of nums1 (n+n elements total)
    while (ptr >= 0) {
        // If neither list has reached the end
        if (m >= 0 && n >= 0) {
            // If nums1[m] is greater than nums2[n], insert nums1[m] at nums1[ptr], decrement ptr and m.
            if (nums1[m] > nums2[n]) { 
                nums1[ptr--] = nums1[m--]; 
            } else // nums1[m] < nums2[n]
            {
                // insert nums2[n] at nums1[ptr], decrement ptr and n
                nums1[ptr--] = nums2[n--];
            }
        // If nums1's index (m) reached the end, then insert nums2[n] at nums1[ptr] and decrement ptr and n
        } else if(m<0) nums1[ptr--] = nums2[n--];
        // If nums2's index reached the end, then insert nums1[m].
        else nums1[ptr--] = nums1[m--]; 
    }
}