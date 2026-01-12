# Last updated: 1/12/2026, 3:13:02 PM
class Solution(object):
    def minZeroArray(self, nums, queries):
        

        def can_zero_with_k_queries(k):
            prefix_sum_array = [0] * (len(nums)+1) #extra spot for buffer
            for query in queries[:k]: #create prefix sum array
                left, right, val = query #deconstruct
                prefix_sum_array[left] += val
                prefix_sum_array[right + 1] -= val

            updating_sum = 0
            pre = []

            for prefix in prefix_sum_array:
                updating_sum += prefix
                pre.append(updating_sum)

            for prefix, num in zip(pre, nums):
                if num > prefix: #we need more queries
                    return False
            return True

        low, high = 0, len(queries)
        res = -1
        while low <= high:
            m = (low + high) // 2
            if can_zero_with_k_queries(m):
                res = m
                high = m - 1
            else: low = m + 1

        return res