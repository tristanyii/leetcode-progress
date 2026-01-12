# Last updated: 1/12/2026, 3:13:11 PM
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        #k multiplication operations

        #perform k operations on nums

        #minheap

        minheap = []

        for i in range(len(nums)):
            heapq.heappush(minheap, (nums[i], i))
        
        for i in range(k):
            minval, index = heapq.heappop(minheap)
            heapq.heappush(minheap, (minval*multiplier, index))

        res = nums
        while minheap:
            val, index = heapq.heappop(minheap)
            res[index]=val
        
        return res



        
        