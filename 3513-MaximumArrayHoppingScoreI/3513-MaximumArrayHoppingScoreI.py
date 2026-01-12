# Last updated: 1/12/2026, 3:13:12 PM
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ret = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                ret[i] = max(ret[i], ret[j] + (i-j)*nums[i])
                #print(ret)
            #print("---")

        return ret[-1]