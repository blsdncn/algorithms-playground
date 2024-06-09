import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # If k equals the length of the list, return the smallest element in the list
        if k == len(nums):
            return min(nums)
        
        # Create a min-heap with the first k elements of the list
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate through the remaining elements in the list
        for elem in nums[k:]:
            # If the current element is greater than the smallest element in the heap
            if elem > min_heap[0]:
                # Remove the smallest element from the heap
                heapq.heappop(min_heap)
                # Add the current element to the heap
                heapq.heappush(min_heap, elem)
        
        # Return the smallest element in the heap, which is the k-th largest element in the list
        return min_heap[0]