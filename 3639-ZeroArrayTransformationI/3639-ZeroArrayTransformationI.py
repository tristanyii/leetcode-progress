# Last updated: 1/12/2026, 3:13:05 PM
class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
    
        dArray = [0]*(len(nums)+1)
        for l,r in queries:
            dArray[l] += 1
            dArray[r+1] -= 1
        
        num_ops = []
        append_num = 0
        for num in dArray:
            append_num += num
            num_ops.append(append_num)

        for sum_minus, target in zip(num_ops, nums):
            if sum_minus < target:
                return False
        return True