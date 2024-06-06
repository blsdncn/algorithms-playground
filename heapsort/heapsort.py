class Solution(object):
    def swap(self, list, i, j):
        list[i], list[j] = list[j], list[i]

    def siftDown(self, list, i, upper):
        while True:
            l, r = i * 2 + 1, i * 2 + 2
            if max(l, r) < upper:
                if list[i] >= max(list[l], list[r]): 
                    break
                elif list[l] > list[r]:
                    self.swap(list, i, l)
                    i = l
                else:
                    self.swap(list, i, r)
                    i = r
            elif l < upper:
                if list[l] > list[i]:
                    self.swap(list, i, l)
                    i = l
                else: 
                    break
            elif r < upper:
                if list[r] > list[i]:
                    self.swap(list, i, r)
                    i = r
                else: 
                    break
            else: 
                break

    def heapsort(self, list):
        for j in range((len(list) - 2) // 2, -1, -1):
            self.siftDown(list, j, len(list))
        
        for end in range(len(list) - 1, 0, -1):
            self.swap(list, 0, end)
            self.siftDown(list, 0, end)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.heapsort(nums)
        return nums
