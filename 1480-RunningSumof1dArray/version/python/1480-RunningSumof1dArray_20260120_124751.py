# Last updated: 1/20/2026, 12:47:51 PM
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        prefix = [0]
4        
5        for num in nums:
6            prefix.append(prefix[-1] + num)
7            
8        return prefix[1:]
9        