# Last updated: 1/12/2026, 3:13:13 PM
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        ret = -float('inf')
        tot = sum(nums)
        c = Counter(nums)
        for n in nums:
            if (tot-n)%2 == 0:
                if (tot-n)//2 in c:
                    if n == (tot-n)//2:
                        if c[(tot-n)//2] > 1:
                            ret = max(ret, n)
                    else:
                        ret = max(ret, n)
        
        return ret
